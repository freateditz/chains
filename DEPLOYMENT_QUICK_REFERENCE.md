# 📋 **RENDER DEPLOYMENT QUICK REFERENCE CARD**

## 🚀 **SERVICE CONFIGURATIONS AT A GLANCE**

### **1️⃣ AI SERVICE (Python)**
```yaml
Type: Web Service
Name: justicechain-ai
Environment: Python 3
Root Directory: AI
Build Command: pip install -r requirements.txt
Start Command: python connect.py
Health Check: /classify
Plan: Starter ($7/month)

Environment Variables:
GROQ_API_KEY=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
PORT=5050
FLASK_ENV=production
```

---

### **2️⃣ BACKEND (Node.js)**
```yaml
Type: Web Service  
Name: justicechain-backend
Environment: Node
Root Directory: backend
Build Command: npm install
Start Command: npm start
Health Check: /api
Plan: Starter ($7/month)

Environment Variables:
MONGO_URL=mongodb+srv://JusticeChain:justicechain2829@cluster0.b6ko82w.mongodb.net/JusticeChain?retryWrites=true&w=majority&appName=Cluster0
NFT_STORAGE_API_KEY=53e149c4.4fda37d017644de79cb876e369c17ebd
PORT=5000
NODE_ENV=production
```

---

### **3️⃣ BLOCKCHAIN BACKEND (Node.js)**
```yaml
Type: Web Service
Name: justicechain-blockchain  
Environment: Node
Root Directory: blockchainbackend
Build Command: npm install
Start Command: npm start
Health Check: /
Plan: Starter ($7/month)

Environment Variables:
PINATA_API_KEY=cc8fe42e71e224398f99
PINATA_SECRET_API_KEY=af5c1aec92580ed58c924a2b7fa4c8cb4688c463071e35359510115e4394c210
PRIVATE_KEY=a3a711b3ce1f86a929dcc4ed6412ba8b9631edeb261309e97d3fcbfcad35a0f5
RPC_URL=https://sepolia.infura.io/v3/542f1eaa832d48f7b99c34caca33add7
CONTRACT_ADDRESS=0xF23133f1cd75C8AF6dEe73389BbB4C327697B82D
AI_SERVICE_URL=https://[YOUR-AI-SERVICE-URL].onrender.com
PORT=4000
NODE_ENV=production
```

---

### **4️⃣ FRONTEND (React Static)**
```yaml
Type: Static Site
Name: justicechain-frontend
Root Directory: frontend
Build Command: yarn install && yarn build
Publish Directory: build
Plan: FREE

Environment Variables:
REACT_APP_BACKEND_URL=https://[YOUR-BACKEND-URL].onrender.com
REACT_APP_BLOCKCHAIN_BACKEND_URL=https://[YOUR-BLOCKCHAIN-URL].onrender.com
REACT_APP_AI_SERVICE_URL=https://[YOUR-AI-URL].onrender.com

Redirects/Rewrites:
Source: /*
Destination: /index.html
Action: Rewrite
```

---

## ⚡ **QUICK DEPLOYMENT STEPS**

### **Deploy Order**: AI → Backend → Blockchain → Frontend

```bash
1. AI Service     → Get URL → Use in Blockchain
2. Backend        → Get URL → Use in Frontend  
3. Blockchain     → Get URL → Use in Frontend
4. Frontend       → Update all URLs → Final deployment
```

---

## 🧪 **QUICK TEST COMMANDS**

### **Test AI Service**
```bash
curl -X POST https://YOUR-AI-URL.onrender.com/classify \
  -H "Content-Type: application/json" \
  -d '{"incidentDescription": "Someone stole my phone"}'
```

### **Test Backend**
```bash
curl -X POST https://YOUR-BACKEND-URL.onrender.com/api/auth/citizen/register \
  -H "Content-Type: application/json" \
  -d '{"fullName":"Test","email":"test@example.com","phone":"9876543210","password":"test123"}'
```

### **Test Blockchain**
```bash
curl https://YOUR-BLOCKCHAIN-URL.onrender.com
```

### **Test Frontend**
```bash
# Visit in browser
https://YOUR-FRONTEND-URL.onrender.com
```

---

## 📝 **ENVIRONMENT VARIABLES TEMPLATE**

### **Copy-Paste Format for Each Service**

**AI Service:**
```
GROQ_API_KEY=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
PORT=5050
FLASK_ENV=production
```

**Backend:**
```
MONGO_URL=mongodb+srv://JusticeChain:justicechain2829@cluster0.b6ko82w.mongodb.net/JusticeChain?retryWrites=true&w=majority&appName=Cluster0
NFT_STORAGE_API_KEY=53e149c4.4fda37d017644de79cb876e369c17ebd
PORT=5000
NODE_ENV=production
```

**Blockchain:**
```
PINATA_API_KEY=cc8fe42e71e224398f99
PINATA_SECRET_API_KEY=af5c1aec92580ed58c924a2b7fa4c8cb4688c463071e35359510115e4394c210
PRIVATE_KEY=a3a711b3ce1f86a929dcc4ed6412ba8b9631edeb261309e97d3fcbfcad35a0f5
RPC_URL=https://sepolia.infura.io/v3/542f1eaa832d48f7b99c34caca33add7
CONTRACT_ADDRESS=0xF23133f1cd75C8AF6dEe73389BbB4C327697B82D
AI_SERVICE_URL=REPLACE_WITH_YOUR_AI_URL
PORT=4000
NODE_ENV=production
```

**Frontend:**
```
REACT_APP_BACKEND_URL=REPLACE_WITH_YOUR_BACKEND_URL
REACT_APP_BLOCKCHAIN_BACKEND_URL=REPLACE_WITH_YOUR_BLOCKCHAIN_URL  
REACT_APP_AI_SERVICE_URL=REPLACE_WITH_YOUR_AI_URL
```

---

## 🎯 **SUCCESS INDICATORS**

| Service | Success Response |
|---------|------------------|
| **AI** | `{"priority": "medium"}` |
| **Backend** | Registration success or user exists |
| **Blockchain** | `"JusticeChain Backend Running"` |
| **Frontend** | App loads without console errors |

---

## 💰 **COST BREAKDOWN**
```
AI Service:      $7/month
Backend:         $7/month  
Blockchain:      $7/month
Frontend:        FREE
                --------
TOTAL:          $21/month
```

---

## 🆘 **QUICK FIXES**

### **Build Fails?**
- Check Root Directory spelling
- Verify Build Command syntax
- Ensure dependencies files exist

### **Start Fails?**
- Check Start Command
- Verify environment variables
- Check service logs

### **Can't Connect?**
- Verify all services are "Live"
- Check environment variable URLs
- Test with curl commands

---

## ✅ **DEPLOYMENT CHECKLIST**

- [ ] AI Service deployed and responding
- [ ] Backend service deployed and connects to MongoDB
- [ ] Blockchain service deployed and connects to AI
- [ ] Frontend deployed with all service URLs updated
- [ ] End-to-end FIR filing works
- [ ] AI classification returns correct severity
- [ ] All services show "Live" status

**🎉 Ready to use your deployed JusticeChain application!**