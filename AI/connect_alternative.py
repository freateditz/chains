print("Starting Flask AI Server...")
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Get API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print("Loaded API key:", GROQ_API_KEY[:20] + "..." if GROQ_API_KEY else "Not found")

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "AI service is running", "api_key_configured": bool(GROQ_API_KEY)})

@app.route('/classify', methods=['POST'])
def classify_fir():
    if not GROQ_API_KEY:
        return jsonify({"error": "GROQ API key not configured"}), 500
        
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
        # Use requests instead of groq library
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "llama3-8b-8192",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0,
            "max_tokens": 10
        }
        
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code != 200:
            print(f"Groq API error: {response.status_code} - {response.text}")
            return jsonify({"error": f"Groq API error: {response.status_code}"}), 500
        
        response_data = response.json()
        priority = response_data["choices"][0]["message"]["content"].strip()
        
        print("AI Response:", priority)
        priority = priority.lower()
        
        if "high" in priority:
            priority = "high"
        elif "medium" in priority:
            priority = "medium"
        elif "low" in priority:
            priority = "low"
        else:
            priority = 'low'
        
        print("Final processed priority:", priority)

        return jsonify({"priority": priority})
        
    except requests.exceptions.RequestException as e:
        print(f"Network error in AI classification: {e}")
        return jsonify({"error": "Network error connecting to AI service"}), 500
    except Exception as e:
        print(f"Error in AI classification: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5050))
    print(f"Starting AI server on port {port}")
    app.run(host="0.0.0.0", debug=False, port=port)