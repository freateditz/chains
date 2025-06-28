# 🚀 **COMPLETE RENDER DEPLOYMENT GUIDE - DETAILED CONFIGURATIONS**

## 📋 **DEPLOYMENT OVERVIEW**

**Total Services to Deploy**: 4
**Deployment Order**: AI Service → Backend → Blockchain Backend → Frontend
**Total Time**: ~15-20 minutes
**Total Cost**: $21/month (3 web services @ $7 each + 1 free static site)

---

## 🤖 **SERVICE 1: AI SERVICE (Python/Flask)**

### **Step 1.1: Create Web Service**
1. **Login to Render Dashboard**: [https://dashboard.render.com](https://dashboard.render.com)
2. **Click "New +"** (top right corner)
3. **Select "Web Service"**
4. **Connect Repository**:
   - Click "Connect a repository"
   - Choose "Connect GitHub" (or your git provider)
   - Select your JusticeChain repository
   - Click "Connect"

### **Step 1.2: Basic Configuration**
```yaml
Service name: justicechain-ai
Environment: Python 3
Region: Oregon (US West) [Recommended for cost/performance]
Branch: main
```

### **Step 1.3: Build & Deploy Settings**
```yaml
Root Directory: AI
Build Command: pip install -r requirements.txt
Start Command: python connect.py
```

**⚠️ IMPORTANT**: 
- Root Directory is `AI` (exactly as shown, case sensitive)
- Build Command installs Python dependencies
- Start Command runs the Flask application

### **Step 1.4: Environment Variables**
Click "Advanced" → "Add Environment Variable"

| Key | Value |
|-----|-------|
| `GROQ_API_KEY` | `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` |
| `PORT` | `5050` |
| `FLASK_ENV` | `production` |

### **Step 1.5: Advanced Settings**
```yaml
Instance Type: Starter (512 MB RAM, 0.1 CPU)
Auto-Deploy: Yes ✓
Health Check Path: /classify (optional)
```

### **Step 1.6: Deploy AI Service**
1. **Click "Create Web Service"**
2. **Wait 3-4 minutes** for build and deployment
3. **Service URL**: Copy this URL → `https://justicechain-ai-XXXXX.onrender.com`

### **Step 1.7: Test AI Service**
```bash
# Test the AI classification endpoint
curl -X POST https://YOUR-AI-SERVICE-URL.onrender.com/classify \
  -H "Content-Type: application/json" \
  -d '{"incidentDescription": "Someone stole my car"}'

# Expected Response:
# {"priority": "medium"}
```

**✅ Success Criteria**: Service status shows "Live" and test returns JSON response

---

## 🗄️ **SERVICE 2: BACKEND (Node.js + MongoDB)**

### **Step 2.1: Create Web Service**
1. **Click "New +"** → **"Web Service"**
2. **Connect same repository** (should be easier the second time)

### **Step 2.2: Basic Configuration**
```yaml
Service name: justicechain-backend
Environment: Node
Region: Oregon (US West) [Same as AI service]
Branch: main
```

### **Step 2.3: Build & Deploy Settings**
```yaml
Root Directory: backend
Build Command: npm install
Start Command: npm start
```

**⚠️ IMPORTANT**: 
- Root Directory is `backend` (exactly as shown)
- Build Command installs Node.js dependencies
- Start Command uses package.json scripts

### **Step 2.4: Environment Variables**
Click "Advanced" → "Add Environment Variable"

| Key | Value |
|-----|-------|
| `MONGO_URL` | `mongodb+srv://JusticeChain:justicechain2829@cluster0.b6ko82w.mongodb.net/JusticeChain?retryWrites=true&w=majority&appName=Cluster0` |
| `NFT_STORAGE_API_KEY` | `53e149c4.4fda37d017644de79cb876e369c17ebd` |
| `PORT` | `5000` |
| `NODE_ENV` | `production` |

### **Step 2.5: Advanced Settings**
```yaml
Instance Type: Starter (512 MB RAM, 0.1 CPU)
Auto-Deploy: Yes ✓
Health Check Path: /api (optional)
```

### **Step 2.6: Deploy Backend Service**
1. **Click "Create Web Service"**
2. **Wait 2-3 minutes** for build and deployment
3. **Service URL**: Copy this URL → `https://justicechain-backend-XXXXX.onrender.com`

### **Step 2.7: Test Backend Service**
```bash
# Test if backend is running
curl https://YOUR-BACKEND-URL.onrender.com

# Test MongoDB connection (should return method not allowed but confirms service is up)
curl -X POST https://YOUR-BACKEND-URL.onrender.com/api/auth/citizen/register \
  -H "Content-Type: application/json" \
  -d '{
    "fullName": "Test User",
    "email": "test@example.com",
    "phone": "9876543210",
    "password": "testpass123"
  }'

# Expected: Should return success or user already exists
```

**✅ Success Criteria**: Service status shows "Live" and registration endpoint responds

---

## ⛓️ **SERVICE 3: BLOCKCHAIN BACKEND (Node.js + Ethereum)**

### **Step 3.1: Create Web Service**
1. **Click "New +"** → **"Web Service"**
2. **Connect same repository**

### **Step 3.2: Basic Configuration**
```yaml
Service name: justicechain-blockchain
Environment: Node
Region: Oregon (US West) [Same region as other services]
Branch: main
```

### **Step 3.3: Build & Deploy Settings**
```yaml
Root Directory: blockchainbackend
Build Command: npm install
Start Command: npm start
```

**⚠️ IMPORTANT**: 
- Root Directory is `blockchainbackend` (exactly as shown)
- This service depends on AI service URL from Step 1

### **Step 3.4: Environment Variables**
⚠️ **CRITICAL**: Replace `YOUR-AI-SERVICE-URL` with actual URL from Step 1!

| Key | Value |
|-----|-------|
| `PINATA_API_KEY` | `cc8fe42e71e224398f99` |
| `PINATA_SECRET_API_KEY` | `af5c1aec92580ed58c924a2b7fa4c8cb4688c463071e35359510115e4394c210` |
| `PRIVATE_KEY` | `a3a711b3ce1f86a929dcc4ed6412ba8b9631edeb261309e97d3fcbfcad35a0f5` |
| `RPC_URL` | `https://sepolia.infura.io/v3/542f1eaa832d48f7b99c34caca33add7` |
| `CONTRACT_ADDRESS` | `0xF23133f1cd75C8AF6dEe73389BbB4C327697B82D` |
| `AI_SERVICE_URL` | `https://justicechain-ai-XXXXX.onrender.com` |
| `PORT` | `4000` |
| `NODE_ENV` | `production` |

**🔧 How to get AI_SERVICE_URL**:
1. Go to your AI service in Render dashboard
2. Copy the URL at the top (should look like: `https://justicechain-ai-xxxxx.onrender.com`)
3. Paste it as the value for `AI_SERVICE_URL`

### **Step 3.5: Advanced Settings**
```yaml
Instance Type: Starter (512 MB RAM, 0.1 CPU)
Auto-Deploy: Yes ✓
Health Check Path: /
```

### **Step 3.6: Deploy Blockchain Service**
1. **Click "Create Web Service"**
2. **Wait 2-3 minutes** for build and deployment
3. **Service URL**: Copy this URL → `https://justicechain-blockchain-XXXXX.onrender.com`

### **Step 3.7: Test Blockchain Service**
```bash
# Test if blockchain service is running
curl https://YOUR-BLOCKCHAIN-URL.onrender.com

# Expected Response: "JusticeChain Backend Running"

# Test AI integration
curl -X POST https://YOUR-BLOCKCHAIN-URL.onrender.com/api/uploadFIR \
  -H "Content-Type: application/json" \
  -d '{
    "incidentType": "Test",
    "incidentDescription": "Test incident for AI classification",
    "incidentLocation": "Test Location",
    "fullName": "Test User",
    "severity": 2
  }'

# Should return success with transaction hash
```

**✅ Success Criteria**: Service status shows "Live" and returns "JusticeChain Backend Running"

---

## 🌐 **SERVICE 4: FRONTEND (React Static Site)**

### **Step 4.1: Create Static Site**
1. **Click "New +"** → **"Static Site"** (NOT Web Service!)
2. **Connect same repository**

### **Step 4.2: Basic Configuration**
```yaml
Site name: justicechain-frontend
Branch: main
```

### **Step 4.3: Build & Deploy Settings**
⚠️ **CRITICAL**: Replace ALL URLs with your actual service URLs from previous steps!

```yaml
Root Directory: frontend
Build Command: yarn install && yarn build
Publish Directory: build
```

**⚠️ IMPORTANT**: 
- Root Directory is `frontend` (exactly as shown)
- Build Command uses yarn (not npm) for better performance
- Publish Directory is `build` (React's output folder)

### **Step 4.4: Environment Variables**
⚠️ **CRITICAL**: You MUST replace these URLs with your actual service URLs!

| Key | Value |
|-----|-------|
| `REACT_APP_BACKEND_URL` | `https://justicechain-backend-XXXXX.onrender.com` |
| `REACT_APP_BLOCKCHAIN_BACKEND_URL` | `https://justicechain-blockchain-XXXXX.onrender.com` |
| `REACT_APP_AI_SERVICE_URL` | `https://justicechain-ai-XXXXX.onrender.com` |

**🔧 How to get these URLs**:
1. **Backend URL**: Go to your backend service → Copy URL
2. **Blockchain URL**: Go to your blockchain service → Copy URL  
3. **AI URL**: Go to your AI service → Copy URL

### **Step 4.5: Redirects & Rewrites (REQUIRED for React Router)**
Click "Advanced" → "Redirects and Rewrites" → "Add Rule"

```yaml
Source: /*
Destination: /index.html
Action: Rewrite
```

**⚠️ CRITICAL**: This is required for React Router to work properly on refresh!

### **Step 4.6: Advanced Settings**
```yaml
Instance Type: N/A (Static sites don't have instance types)
Auto-Deploy: Yes ✓
```

### **Step 4.7: Deploy Frontend**
1. **Click "Create Static Site"**
2. **Wait 4-5 minutes** for build and deployment
3. **Site URL**: Your live app → `https://justicechain-frontend-XXXXX.onrender.com`

### **Step 4.8: Test Frontend**
1. **Visit your frontend URL** in browser
2. **Check for any console errors** (F12 → Console)
3. **Try registering** as a citizen
4. **Try logging in**
5. **Test FIR filing** (optional at this stage)

**✅ Success Criteria**: Frontend loads without errors and registration works

---

## 🔄 **STEP 5: UPDATE SERVICE URLs (CRITICAL)**

After all services are deployed, you need to update URLs with actual values:

### **Step 5.1: Update Frontend Environment Variables**
1. **Go to Frontend Static Site** in Render dashboard
2. **Click "Environment" tab**
3. **Update environment variables** with your actual URLs:

| Key | Current Value | New Value (Your Actual URLs) |
|-----|---------------|-------------------------------|
| `REACT_APP_BACKEND_URL` | `https://justicechain-backend-XXXXX.onrender.com` | **YOUR ACTUAL BACKEND URL** |
| `REACT_APP_BLOCKCHAIN_BACKEND_URL` | `https://justicechain-blockchain-XXXXX.onrender.com` | **YOUR ACTUAL BLOCKCHAIN URL** |
| `REACT_APP_AI_SERVICE_URL` | `https://justicechain-ai-XXXXX.onrender.com` | **YOUR ACTUAL AI URL** |

4. **Click "Save Changes"**
5. **Wait for automatic rebuild** (3-4 minutes)

### **Step 5.2: Update Blockchain Backend (If Needed)**
1. **Go to Blockchain Backend Web Service**
2. **Click "Environment" tab**
3. **Verify AI_SERVICE_URL** is correct
4. **If wrong, update and save**

---

## ✅ **STEP 6: COMPREHENSIVE TESTING**

### **Test 1: Individual Service Health**
```bash
# Test AI Service
curl -X POST https://YOUR-AI-URL.onrender.com/classify \
  -H "Content-Type: application/json" \
  -d '{"incidentDescription": "Armed robbery"}'
# Expected: {"priority": "high"}

# Test Backend Service  
curl https://YOUR-BACKEND-URL.onrender.com
# Expected: Some response (not error)

# Test Blockchain Service
curl https://YOUR-BLOCKCHAIN-URL.onrender.com
# Expected: "JusticeChain Backend Running"
```

### **Test 2: End-to-End Application Flow**
1. **Visit Frontend URL** in browser
2. **Register as Citizen**:
   - Full Name: Test User
   - Email: test@example.com
   - Phone: 9876543210
   - Password: testpass123

3. **Login with same credentials**
4. **File a Test FIR**:
   - Use crime description: "Someone stole my laptop"
   - Fill required fields
   - Submit FIR
   - Check for success message with severity

### **Test 3: AI Classification Integration**
1. **File FIR with high priority crime**: "Armed robbery at gunpoint"
2. **Check browser console** (F12) for:
   ```
   AI Raw Response: {priority: "high"}
   Final severity calculated: 3
   ```
3. **Verify success message** shows correct severity

---

## 📊 **DEPLOYMENT SUMMARY TABLE**

| Service | Type | URL Format | Build Time | Status |
|---------|------|------------|------------|--------|
| **AI Service** | Web Service | `https://justicechain-ai-[id].onrender.com` | 3-4 min | ✅ |
| **Backend** | Web Service | `https://justicechain-backend-[id].onrender.com` | 2-3 min | ✅ |
| **Blockchain** | Web Service | `https://justicechain-blockchain-[id].onrender.com` | 2-3 min | ✅ |
| **Frontend** | Static Site | `https://justicechain-frontend-[id].onrender.com` | 4-5 min | ✅ |

**Total Cost**: $21/month (Frontend is FREE!)

---

## 🆘 **DETAILED TROUBLESHOOTING**

### **Issue: Build Fails**
**Check These**:
```yaml
✓ Root Directory is exactly correct (case sensitive)
✓ Build Command syntax is correct
✓ package.json/requirements.txt exists in root directory
✓ Dependencies are properly listed
```

**Common Build Command Issues**:
- AI Service: `pip install -r requirements.txt` (not `pip3`)
- Backend: `npm install` (not `yarn install`)
- Blockchain: `npm install` (not `yarn install`)
- Frontend: `yarn install && yarn build` (not `npm`)

### **Issue: Service Won't Start**
**Check These**:
```yaml
✓ Start Command is correct
✓ All environment variables are set
✓ PORT environment variable matches service expectations
✓ Service logs for specific error messages
```

**Common Start Command Issues**:
- AI Service: `python connect.py` (not `python3`)
- Backend: `npm start` (requires "start" script in package.json)
- Blockchain: `npm start` (requires "start" script in package.json)

### **Issue: Frontend Can't Connect to Backend**
**Solutions**:
```yaml
1. Verify all backend services show "Live" status
2. Check environment variables have correct URLs (no typos)
3. Test backend URLs directly with curl
4. Check browser console for CORS errors
5. Verify redirects/rewrites are configured for React Router
```

### **Issue: Environment Variables Not Working**
**Solutions**:
```yaml
1. Environment variable names are EXACTLY correct (case sensitive)
2. No extra spaces in variable names or values
3. All required variables are set
4. Restart service after adding variables
5. Check service logs for "undefined" errors
```

---

## 🎯 **SUCCESS CHECKLIST**

### **Deployment Complete When**:
- [ ] ✅ All 4 services show "Live" status in Render dashboard
- [ ] ✅ All service URLs are accessible and return expected responses
- [ ] ✅ Frontend loads without console errors
- [ ] ✅ User registration and login works
- [ ] ✅ FIR filing process completes successfully
- [ ] ✅ AI classification returns appropriate severity levels
- [ ] ✅ Blockchain transaction completes with correct severity
- [ ] ✅ No CORS or network errors in browser console

### **Performance Indicators**:
- [ ] ✅ Services respond within 2-3 seconds (first request may be slower due to cold start)
- [ ] ✅ AI classification completes within 5 seconds
- [ ] ✅ Blockchain transaction completes within 30 seconds
- [ ] ✅ Frontend navigation is smooth and responsive

---

## 🎉 **CONGRATULATIONS!**

Your JusticeChain application is now fully deployed and live!

**🌍 Your Live Application**: `https://justicechain-frontend-[your-id].onrender.com`

**📱 Features Working**:
- ✅ Citizen Registration & Login
- ✅ Admin Registration & Login  
- ✅ AI-Powered FIR Classification
- ✅ Blockchain Storage with IPFS
- ✅ Real-time Severity Calculation
- ✅ Secure MongoDB Data Storage

**💰 Monthly Cost**: $21 (3 web services @ $7 each + 1 free static site)

**🔧 Management**: All services can be independently scaled, monitored, and updated through the Render dashboard.

Share your live application URL and start using your decentralized justice system! 🚀