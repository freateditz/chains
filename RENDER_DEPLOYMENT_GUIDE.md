# JusticeChain - Render Deployment Guide

## 🚀 Complete Step-by-Step Deployment Guide for Render

### **Overview**
JusticeChain is a comprehensive FIR management system with 4 components:
- **Frontend**: React Static Site
- **Backend**: Node.js/Express + MongoDB
- **Blockchain Backend**: Node.js/Express + Ethereum
- **AI Service**: Python/Flask + GROQ API

---

## **📋 Prerequisites**
1. **Render Account**: Sign up at [render.com](https://render.com)
2. **GitHub Repository**: Your code should be in a GitHub repository
3. **Domain Names** (Optional): For custom domains

---

## **🔧 Method 1: Single-Click Deployment (Recommended)**

### **Step 1: Fork/Clone Repository to GitHub**
1. Ensure your JusticeChain code is in a GitHub repository
2. Your repository should have this structure:
   ```
   /
   ├── frontend/          # React app
   ├── backend/           # Node.js backend
   ├── blockchainbackend/ # Blockchain service
   ├── AI/                # Python AI service
   └── render.yaml        # Render configuration
   ```

### **Step 2: Deploy Using Render Blueprint**
1. **Login to Render Dashboard**
2. **Click "New +"** in top right corner
3. **Select "Blueprint"**
4. **Connect GitHub Repository**:
   - Choose your JusticeChain repository
   - Authorize Render to access your repo
5. **Deploy Services**:
   - Render will automatically read `render.yaml`
   - All 4 services will be created simultaneously
   - Wait 10-15 minutes for complete deployment

### **Step 3: Verify Deployment URLs**
After deployment, you'll get these URLs:
- **Frontend**: `https://justicechain-frontend.onrender.com`
- **Backend**: `https://justicechain-backend.onrender.com`
- **Blockchain**: `https://justicechain-blockchain.onrender.com`
- **AI Service**: `https://justicechain-ai.onrender.com`

---

## **🔧 Method 2: Manual Service Creation**

### **Step 1: Deploy AI Service (Python/Flask)**
1. **Create Web Service**:
   - Service Name: `justicechain-ai`
   - Runtime: `Python 3`
   - Build Command: `cd AI && pip install -r requirements.txt`
   - Start Command: `cd AI && python connect.py`

2. **Environment Variables**:
   ```
   GROQ_API_KEY=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
   PORT=5050
   ```

### **Step 2: Deploy Backend (Node.js + MongoDB)**
1. **Create Web Service**:
   - Service Name: `justicechain-backend`
   - Runtime: `Node`
   - Build Command: `cd backend && npm install`
   - Start Command: `cd backend && npm start`

2. **Environment Variables**:
   ```
   MONGO_URL=mongodb+srv://JusticeChain:justicechain2829@cluster0.b6ko82w.mongodb.net/JusticeChain?retryWrites=true&w=majority&appName=Cluster0
   NFT_STORAGE_API_KEY=53e149c4.4fda37d017644de79cb876e369c17ebd
   PORT=5000
   ```

### **Step 3: Deploy Blockchain Backend (Node.js + Ethereum)**
1. **Create Web Service**:
   - Service Name: `justicechain-blockchain`
   - Runtime: `Node`
   - Build Command: `cd blockchainbackend && npm install`
   - Start Command: `cd blockchainbackend && node index.js`

2. **Environment Variables**:
   ```
   PINATA_API_KEY=cc8fe42e71e224398f99
   PINATA_SECRET_API_KEY=af5c1aec92580ed58c924a2b7fa4c8cb4688c463071e35359510115e4394c210
   PRIVATE_KEY=a3a711b3ce1f86a929dcc4ed6412ba8b9631edeb261309e97d3fcbfcad35a0f5
   RPC_URL=https://sepolia.infura.io/v3/542f1eaa832d48f7b99c34caca33add7
   CONTRACT_ADDRESS=0xF23133f1cd75C8AF6dEe73389BbB4C327697B82D
   AI_SERVICE_URL=https://justicechain-ai.onrender.com
   PORT=4000
   ```

### **Step 4: Deploy Frontend (React Static Site)**
1. **Create Static Site**:
   - Service Name: `justicechain-frontend`
   - Build Command: `cd frontend && yarn install && yarn build`
   - Publish Directory: `frontend/build`

2. **Environment Variables**:
   ```
   REACT_APP_BACKEND_URL=https://justicechain-backend.onrender.com
   REACT_APP_BLOCKCHAIN_BACKEND_URL=https://justicechain-blockchain.onrender.com
   REACT_APP_AI_SERVICE_URL=https://justicechain-ai.onrender.com
   ```

---

## **⚙️ Service Configuration Details**

### **Service Order (Important)**
Deploy in this order to avoid dependency issues:
1. **AI Service** (Independent)
2. **Backend** (Independent) 
3. **Blockchain Backend** (Depends on AI Service)
4. **Frontend** (Depends on all backend services)

### **Resource Requirements**
- **All Services**: Starter Plan (512MB RAM, 0.1 CPU) is sufficient
- **Estimated Monthly Cost**: ~$28/month ($7 per service)

### **Build Times**
- **AI Service**: 3-4 minutes
- **Backend Services**: 2-3 minutes each
- **Frontend**: 4-5 minutes
- **Total Initial Deployment**: 10-15 minutes

---

## **🔗 Service URLs and Communication**

### **Production URLs** (Replace with your actual Render URLs)
```
Frontend:    https://justicechain-frontend.onrender.com
Backend:     https://justicechain-backend.onrender.com  
Blockchain:  https://justicechain-blockchain.onrender.com
AI Service:  https://justicechain-ai.onrender.com
```

### **Service Communication Map**
```
Frontend ──────► Backend (Auth, User Management)
Frontend ──────► Blockchain Backend (FIR Submission)
Blockchain ────► AI Service (Crime Classification)
Backend ───────► MongoDB Atlas (User Data)
Blockchain ────► Ethereum Sepolia (Smart Contracts)
Blockchain ────► Pinata IPFS (File Storage)
```

---

## **🔒 Environment Variables Reference**

### **Frontend (.env.production)**
```bash
REACT_APP_BACKEND_URL=https://justicechain-backend.onrender.com
REACT_APP_BLOCKCHAIN_BACKEND_URL=https://justicechain-blockchain.onrender.com
REACT_APP_AI_SERVICE_URL=https://justicechain-ai.onrender.com
```

### **Backend (.env)**
```bash
MONGO_URL=mongodb+srv://JusticeChain:justicechain2829@cluster0.b6ko82w.mongodb.net/JusticeChain?retryWrites=true&w=majority&appName=Cluster0
NFT_STORAGE_API_KEY=53e149c4.4fda37d017644de79cb876e369c17ebd
PORT=5000
```

### **Blockchain Backend (.env.production)**
```bash
PINATA_API_KEY=cc8fe42e71e224398f99
PINATA_SECRET_API_KEY=af5c1aec92580ed58c924a2b7fa4c8cb4688c463071e35359510115e4394c210
PRIVATE_KEY=a3a711b3ce1f86a929dcc4ed6412ba8b9631edeb261309e97d3fcbfcad35a0f5
RPC_URL=https://sepolia.infura.io/v3/542f1eaa832d48f7b99c34caca33add7
CONTRACT_ADDRESS=0xF23133f1cd75C8AF6dEe73389BbB4C327697B82D
AI_SERVICE_URL=https://justicechain-ai.onrender.com
PORT=4000
```

### **AI Service (.env)**
```bash
GROQ_API_KEY=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
PORT=5050
```

---

## **✅ Testing Your Deployment**

### **Step 1: Test Individual Services**
1. **AI Service**: 
   ```bash
   curl -X POST https://justicechain-ai.onrender.com/classify \
   -H "Content-Type: application/json" \
   -d '{"incidentDescription": "Test crime description"}'
   ```

2. **Backend**:
   ```bash
   curl https://justicechain-backend.onrender.com/api/auth/citizen/register
   ```

3. **Blockchain Backend**:
   ```bash
   curl https://justicechain-blockchain.onrender.com/
   ```

4. **Frontend**: Visit the frontend URL in browser

### **Step 2: Test End-to-End Flow**
1. **Visit Frontend URL**
2. **Register as Citizen**
3. **Login and File FIR**
4. **Verify FIR Submission**

---

## **🔧 Troubleshooting Common Issues**

### **Issue 1: Service Won't Start**
**Solution**: Check logs in Render dashboard:
- Go to service → Logs tab
- Look for dependency/environment variable errors
- Verify all environment variables are set correctly

### **Issue 2: Frontend Can't Connect to Backend**
**Solution**: 
- Verify backend service is running (green status)
- Check CORS configuration in backend
- Verify environment variables in frontend

### **Issue 3: Build Failures**
**Solution**:
- Check build commands are correct
- Verify package.json/requirements.txt files exist
- Check node/python versions

### **Issue 4: Database Connection Errors**
**Solution**:
- Verify MongoDB Atlas connection string
- Check IP whitelist (use 0.0.0.0/0 for Render)
- Test MongoDB connection independently

---

## **⚡ Optimization Tips**

### **Performance**
1. **Enable Caching**: Use Render's CDN for static assets
2. **Service Sleep**: Free tier services sleep after 15 minutes of inactivity
3. **Cold Starts**: First request after sleep takes 30-60 seconds

### **Cost Optimization**
1. **Starter Plan**: Sufficient for development/testing
2. **Standard Plan**: Recommended for production
3. **Custom Domains**: Available on paid plans

### **Security**
1. **Environment Variables**: Never commit API keys to git
2. **HTTPS**: All Render services get free SSL certificates
3. **Access Control**: Use Render's IP allowlisting if needed

---

## **📈 Monitoring & Maintenance**

### **Health Checks**
- Render automatically monitors service health
- Custom health check endpoints can be configured
- Automatic restarts on service failures

### **Logs & Debugging**
- Real-time logs available in Render dashboard
- Log retention: 7 days on free tier, longer on paid plans
- Integration with external logging services available

### **Updates & Deployment**
- **Auto-Deploy**: Enable automatic deployment on git push
- **Manual Deploy**: Deploy specific commits from dashboard
- **Rollback**: Easy rollback to previous deployments

---

## **🎯 Quick Start Checklist**

- [ ] ✅ Code fixes implemented (ports, environment variables)
- [ ] ✅ GitHub repository ready with all code
- [ ] ✅ Render account created
- [ ] ✅ Blueprint deployment initiated OR manual services created
- [ ] ✅ Environment variables configured for all services
- [ ] ✅ Services deployed and running (green status)
- [ ] ✅ Service URLs verified and accessible
- [ ] ✅ End-to-end testing completed
- [ ] ✅ Custom domains configured (optional)

---

## **🆘 Support**

If you encounter issues:
1. **Check Render Status**: [status.render.com](https://status.render.com)
2. **Render Documentation**: [render.com/docs](https://render.com/docs)
3. **Community Forum**: [community.render.com](https://community.render.com)
4. **Support**: Contact Render support for technical issues

---

## **🎉 Success!**

Once deployed, your JusticeChain application will be available at:
**https://justicechain-frontend.onrender.com**

All services are configured to communicate securely over HTTPS with proper CORS handling, environment variable management, and production-ready configurations.