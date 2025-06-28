print("Starting Flask AI Server...")
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Flask app first
app = Flask(__name__)
CORS(app)

# Get API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print("Loaded API key:", GROQ_API_KEY[:20] + "..." if GROQ_API_KEY else "Not found")

# Initialize Groq client with error handling
client = None
try:
    from groq import Groq
    client = Groq(api_key=GROQ_API_KEY)
    print("Groq client initialized successfully")
except Exception as e:
    print(f"Error initializing Groq client: {e}")
    print("Server will start but AI classification will not work")

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "AI service is running", "groq_client": client is not None})

@app.route('/classify', methods=['POST'])
def classify_fir():
    if client is None:
        return jsonify({"error": "Groq client not initialized"}), 500
        
    data = request.json
    description = data.get("incidentDescription", "")

    if not description:
        return jsonify({"error": "No description provided"}), 400
    
    prompt = f"""You are a crime analysis assistant.

Your job is to classify an FIR description into one of the following categories:
- High: Life-threatening crimes such as murder, rape, terrorism, serious assault, bomb threats
- Medium: Significant crimes like robbery, theft, hacking, fraud
- Low: Minor issues such as lost items, noise complaints, or littering

Only respond with a single word: High, Medium, or Low.

FIR Description: {description}
Priority:"""

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=10            
        )

        priority = response.choices[0].message.content.strip()
        print("AI Response:", response.choices[0].message.content)
        priority = priority.lower()
        
        if "high" in priority:
            priority = "high"
        elif "medium" in priority:
            priority = "medium"
        elif "low" in priority:
            priority = "low"
        else:
            priority = 'low'
        
        print("Prompt sent to AI:\n", prompt)
        print("Final processed priority:", priority)

        return jsonify({"priority": priority})
    except Exception as e:
        print(f"Error in AI classification: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5050))
    app.run(host="0.0.0.0", debug=True, port=port)


