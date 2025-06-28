# 📝 Quick Reference - Manual Deployment Commands

## 🚀 **DEPLOYMENT ORDER & COMMANDS**

### **1️⃣ AI SERVICE (Deploy First)**
```yaml
Service Type: Web Service
Name: justicechain-ai
Environment: Python 3
Root Directory: AI
Build Command: pip install -r requirements.txt
Start Command: python connect.py

Environment Variables:
GROQ_API_KEY=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
PORT=5050
```

**Test Command:**
```bash
curl -X POST https://your-ai-url.onrender.com/classify \
  -H "Content-Type: application/json" \
  -d '{"incidentDescription": "Test description"}'
```

---

### **2️⃣ BACKEND SERVICE (Deploy Second)**
```yaml
Service Type: Web Service
Name: justicechain-backend
Environment: Node
Root Directory: backend
Build Command: npm install
Start Command: npm start

Environment Variables:
MONGO_URL=mongodb+srv://JusticeChain:justicechain2829@cluster0.b6ko82w.mongodb.net/JusticeChain?retryWrites=true&w=majority&appName=Cluster0
NFT_STORAGE_API_KEY=53e149c4.4fda37d017644de79cb876e369c17ebd
PORT=5000
NODE_ENV=production
```

**Test Command:**
```bash
curl https://your-backend-url.onrender.com/api/auth/citizen/register \
  -X POST -H "Content-Type: application/json" \
  -d '{"fullName":"Test","email":"test@example.com","phone":"9876543210","password":"test123"}'
```

---

### **3️⃣ BLOCKCHAIN BACKEND (Deploy Third)**
```yaml
Service Type: Web Service
Name: justicechain-blockchain
Environment: Node
Root Directory: blockchainbackend
Build Command: npm install
Start Command: npm start

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

**Test Command:**
```bash
curl https://your-blockchain-url.onrender.com/
# Should return: "JusticeChain Backend Running"
```

---

### **4️⃣ FRONTEND (Deploy Last)**
```yaml
Service Type: Static Site
Name: justicechain-frontend
Root Directory: frontend
Build Command: yarn install && yarn build
Publish Directory: build

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

## 🔄 **QUICK STEPS CHECKLIST**

### **Phase 1: Deploy Services**
- [ ] 1. Deploy AI Service → Get URL
- [ ] 2. Deploy Backend Service → Get URL
- [ ] 3. Deploy Blockchain Service (use AI URL) → Get URL
- [ ] 4. Deploy Frontend (use all URLs) → Get URL

### **Phase 2: Update URLs**
- [ ] 5. Update Frontend env vars with actual service URLs
- [ ] 6. Update Blockchain Backend with actual AI URL
- [ ] 7. Wait for automatic redeployments

### **Phase 3: Test Everything**
- [ ] 8. Test each service individually
- [ ] 9. Test end-to-end application flow
- [ ] 10. Verify all functionality works

---

## 💰 **COST BREAKDOWN**
```
AI Service (Python):      $7/month
Backend (Node.js):        $7/month  
Blockchain (Node.js):     $7/month
Frontend (Static):        FREE
                         --------
TOTAL:                    $21/month
```

---

## 🆘 **QUICK TROUBLESHOOTING**

### **Build Fails?**
- Check logs in Render dashboard
- Verify file paths and build commands
- Ensure dependencies are listed correctly

### **Service Won't Start?**
- Check environment variables are set
- Verify start command is correct
- Look for missing dependencies in logs

### **Can't Connect Services?**
- Verify all services show "Running" status
- Check environment variable URLs are correct
- Test individual services with curl

### **Frontend Errors?**
- Check browser developer console
- Verify backend services are accessible
- Check CORS configuration

---

## 🎯 **SUCCESS INDICATORS**

✅ **All 4 services show "Running" status in Render**
✅ **Frontend loads without console errors**
✅ **Can register and login as citizen**
✅ **Can file FIR successfully**
✅ **AI classification works**
✅ **Blockchain transaction completes**

---

**🚀 Once all services are deployed and tested, your JusticeChain application will be live and fully functional!**