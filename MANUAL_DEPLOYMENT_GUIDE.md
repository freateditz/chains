# 🚀 JusticeChain Manual Deployment Guide - Web Services & Static Sites

## 📋 **MANUAL DEPLOYMENT OVERVIEW**

We'll deploy 4 separate services on Render:
1. **AI Service** (Python Web Service) - Deploy FIRST
2. **Backend** (Node.js Web Service) - Deploy SECOND  
3. **Blockchain Backend** (Node.js Web Service) - Deploy THIRD
4. **Frontend** (Static Site) - Deploy LAST

> **Important**: Deploy in this order to ensure proper service dependencies!

---

## 🔑 **STEP 1: DEPLOY AI SERVICE (Python Web Service)**

### **1.1 Create Web Service**
1. **Login to Render Dashboard**
2. **Click "New +"** → **"Web Service"**
3. **Connect Repository**:
   - Select "Connect a repository"
   - Choose your GitHub repository
   - Click "Connect"

### **1.2 Configure AI Service**
```yaml
Service Name: justicechain-ai
Environment: Python 3
Region: Oregon (US West) or your preferred region
Branch: main (or your default branch)
Root Directory: AI
Build Command: pip install -r requirements.txt
Start Command: python connect.py
```

### **1.3 Environment Variables**
Add these environment variables:
```bash
GROQ_API_KEY=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
PORT=5050
```

### **1.4 Advanced Settings**
```yaml
Plan: Starter ($7/month)
Auto-Deploy: Yes (recommended)
Health Check Path: / (optional)
```

### **1.5 Deploy**
- Click **"Create Web Service"**
- Wait 3-4 minutes for deployment
- ✅ **Service URL**: `https://justicechain-ai-[unique-id].onrender.com`

### **1.6 Test AI Service**
```bash
curl -X POST https://your-ai-service-url.onrender.com/classify \
  -H "Content-Type: application/json" \
  -d '{"incidentDescription": "Test crime description"}'

# Expected response:
# {"priority": "low"}
```

---

## 🗄️ **STEP 2: DEPLOY BACKEND (Node.js Web Service)**

### **2.1 Create Web Service**
1. **Click "New +"** → **"Web Service"**
2. **Connect same repository**

### **2.2 Configure Backend Service**
```yaml
Service Name: justicechain-backend
Environment: Node
Region: Oregon (US West) or same as AI service
Branch: main
Root Directory: backend
Build Command: npm install
Start Command: npm start
```

### **2.3 Environment Variables**
Add these environment variables:
```bash
MONGO_URL=mongodb+srv://JusticeChain:justicechain2829@cluster0.b6ko82w.mongodb.net/JusticeChain?retryWrites=true&w=majority&appName=Cluster0
NFT_STORAGE_API_KEY=53e149c4.4fda37d017644de79cb876e369c17ebd
PORT=5000
NODE_ENV=production
```

### **2.4 Advanced Settings**
```yaml
Plan: Starter ($7/month)
Auto-Deploy: Yes
Health Check Path: /api (optional)
```

### **2.5 Deploy**
- Click **"Create Web Service"**
- Wait 2-3 minutes for deployment
- ✅ **Service URL**: `https://justicechain-backend-[unique-id].onrender.com`

### **2.6 Test Backend Service**
```bash
# Test if backend is running
curl https://your-backend-url.onrender.com

# Test MongoDB connection (should return method not allowed but confirms service is up)
curl https://your-backend-url.onrender.com/api/auth/citizen/register
```

---

## ⛓️ **STEP 3: DEPLOY BLOCKCHAIN BACKEND (Node.js Web Service)**

### **3.1 Create Web Service**
1. **Click "New +"** → **"Web Service"**
2. **Connect same repository**

### **3.2 Configure Blockchain Service**
```yaml
Service Name: justicechain-blockchain
Environment: Node
Region: Oregon (US West) or same region as other services
Branch: main
Root Directory: blockchainbackend
Build Command: npm install
Start Command: npm start
```

### **3.3 Environment Variables**
⚠️ **IMPORTANT**: Replace `YOUR_AI_SERVICE_URL` with the actual URL from Step 1!

```bash
PINATA_API_KEY=cc8fe42e71e224398f99
PINATA_SECRET_API_KEY=af5c1aec92580ed58c924a2b7fa4c8cb4688c463071e35359510115e4394c210
PRIVATE_KEY=a3a711b3ce1f86a929dcc4ed6412ba8b9631edeb261309e97d3fcbfcad35a0f5
RPC_URL=https://sepolia.infura.io/v3/542f1eaa832d48f7b99c34caca33add7
CONTRACT_ADDRESS=0xF23133f1cd75C8AF6dEe73389BbB4C327697B82D
AI_SERVICE_URL=https://justicechain-ai-[YOUR-UNIQUE-ID].onrender.com
PORT=4000
NODE_ENV=production
```

### **3.4 Advanced Settings**
```yaml
Plan: Starter ($7/month)
Auto-Deploy: Yes
Health Check Path: / 
```

### **3.5 Deploy**
- Click **"Create Web Service"**
- Wait 2-3 minutes for deployment
- ✅ **Service URL**: `https://justicechain-blockchain-[unique-id].onrender.com`

### **3.6 Test Blockchain Service**
```bash
# Test if blockchain service is running
curl https://your-blockchain-url.onrender.com

# Expected response: "JusticeChain Backend Running"
```

---

## 🌐 **STEP 4: DEPLOY FRONTEND (Static Site)**

### **4.1 Create Static Site**
1. **Click "New +"** → **"Static Site"**
2. **Connect same repository**

### **4.2 Configure Frontend**
```yaml
Site Name: justicechain-frontend
Branch: main
Root Directory: frontend
Build Command: yarn install && yarn build
Publish Directory: build
```

### **4.3 Environment Variables**
⚠️ **IMPORTANT**: Replace URLs with your actual service URLs from previous steps!

```bash
REACT_APP_BACKEND_URL=https://justicechain-backend-[YOUR-UNIQUE-ID].onrender.com
REACT_APP_BLOCKCHAIN_BACKEND_URL=https://justicechain-blockchain-[YOUR-UNIQUE-ID].onrender.com
REACT_APP_AI_SERVICE_URL=https://justicechain-ai-[YOUR-UNIQUE-ID].onrender.com
```

### **4.4 Advanced Settings**
```yaml
Plan: FREE (Static sites are free!)
Auto-Deploy: Yes
Custom Headers: (optional)
Redirects/Rewrites: 
  - Source: /*
  - Destination: /index.html
  - Action: Rewrite
```

### **4.5 Deploy**
- Click **"Create Static Site"**
- Wait 4-5 minutes for build and deployment
- ✅ **Site URL**: `https://justicechain-frontend-[unique-id].onrender.com`

---

## 🔗 **STEP 5: UPDATE SERVICE URLS**

After all services are deployed, you need to update the frontend environment variables with the actual URLs:

### **5.1 Get Your Service URLs**
From your Render Dashboard, copy the URLs for each service:
```
AI Service: https://justicechain-ai-[unique-id].onrender.com
Backend: https://justicechain-backend-[unique-id].onrender.com
Blockchain: https://justicechain-blockchain-[unique-id].onrender.com
```

### **5.2 Update Frontend Environment Variables**
1. Go to your **Frontend Static Site** in Render Dashboard
2. Click **"Environment"** tab
3. Update the environment variables with your actual URLs:
```bash
REACT_APP_BACKEND_URL=https://justicechain-backend-[YOUR-ACTUAL-ID].onrender.com
REACT_APP_BLOCKCHAIN_BACKEND_URL=https://justicechain-blockchain-[YOUR-ACTUAL-ID].onrender.com
REACT_APP_AI_SERVICE_URL=https://justicechain-ai-[YOUR-ACTUAL-ID].onrender.com
```
4. Click **"Save Changes"**
5. Wait for automatic rebuild and redeployment

### **5.3 Update Blockchain Backend Environment Variable**
1. Go to your **Blockchain Backend Web Service** in Render Dashboard
2. Click **"Environment"** tab
3. Update the AI_SERVICE_URL with your actual AI service URL:
```bash
AI_SERVICE_URL=https://justicechain-ai-[YOUR-ACTUAL-ID].onrender.com
```
4. Click **"Save Changes"**
5. Service will automatically restart

---

## ✅ **STEP 6: TESTING & VERIFICATION**

### **6.1 Test Individual Services**

**Test AI Service:**
```bash
curl -X POST https://your-ai-service-url.onrender.com/classify \
  -H "Content-Type: application/json" \
  -d '{"incidentDescription": "Someone stole my phone"}'
```

**Test Backend:**
```bash
curl https://your-backend-url.onrender.com/api/auth/citizen/register \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"fullName":"Test User","email":"test@example.com","phone":"9876543210","password":"testpass"}'
```

**Test Blockchain Backend:**
```bash
curl https://your-blockchain-url.onrender.com/
```

### **6.2 Test Frontend Application**
1. **Visit your frontend URL** in browser
2. **Register as a citizen**
3. **Login with your credentials**
4. **Try to file a FIR**
5. **Verify the complete flow works**

---

## 📊 **DEPLOYMENT SUMMARY**

| Service | Type | URL | Cost | Status |
|---------|------|-----|------|--------|
| AI Service | Web Service | `https://justicechain-ai-[id].onrender.com` | $7/month | ✅ |
| Backend | Web Service | `https://justicechain-backend-[id].onrender.com` | $7/month | ✅ |
| Blockchain | Web Service | `https://justicechain-blockchain-[id].onrender.com` | $7/month | ✅ |
| Frontend | Static Site | `https://justicechain-frontend-[id].onrender.com` | **FREE** | ✅ |
| **TOTAL** | | | **$21/month** | |

---

## 🔧 **TROUBLESHOOTING COMMON ISSUES**

### **Issue: Service Build Fails**
**Solutions:**
```bash
# Check Render logs for specific error
# Common fixes:
1. Verify package.json/requirements.txt exists in correct directory
2. Check build command syntax
3. Verify Node.js/Python version compatibility
4. Check for missing dependencies
```

### **Issue: Frontend Can't Connect to Backend**
**Solutions:**
```bash
1. Verify all backend services are running (green status)
2. Check CORS configuration in backend services
3. Verify environment variables are correct
4. Test backend URLs directly with curl
5. Check browser developer console for network errors
```

### **Issue: Environment Variables Not Working**
**Solutions:**
```bash
1. Ensure environment variables are set in Render dashboard
2. Verify variable names match exactly (case-sensitive)
3. Restart services after adding environment variables
4. Check service logs for environment variable loading
```

### **Issue: MongoDB Connection Error**
**Solutions:**
```bash
1. Verify MongoDB Atlas connection string
2. Whitelist all IPs (0.0.0.0/0) in MongoDB Atlas
3. Check if MongoDB cluster is running
4. Test connection string format
```

---

## 🎯 **SUCCESS CHECKLIST**

- [ ] ✅ AI Service deployed and responding to `/classify` endpoint
- [ ] ✅ Backend service deployed and connects to MongoDB
- [ ] ✅ Blockchain service deployed and can communicate with AI service
- [ ] ✅ Frontend static site deployed and loads without errors
- [ ] ✅ All environment variables correctly configured
- [ ] ✅ Service URLs updated in dependent services
- [ ] ✅ End-to-end user registration works
- [ ] ✅ FIR filing process completes successfully
- [ ] ✅ AI classification returns appropriate priorities
- [ ] ✅ Blockchain transaction completes

---

## 📞 **SUPPORT & MONITORING**

### **Service Health Monitoring**
- Each service has a status indicator in Render dashboard
- Set up email notifications for service failures
- Monitor service logs for errors

### **Performance Optimization**
- Monitor response times and resource usage
- Upgrade to Standard plan if services are slow
- Consider adding custom domains for better branding

### **Cost Management**
- Static site (frontend) remains FREE
- Backend services are $7/month each on Starter plan
- Upgrade to Standard plan ($25/month) for better performance if needed

---

## 🎉 **CONGRATULATIONS!**

Your JusticeChain application is now fully deployed on Render using individual services! 

**Your live application is available at:**
`https://justicechain-frontend-[your-id].onrender.com`

All services are independently managed and can be scaled, monitored, and updated separately as needed.