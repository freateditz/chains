# 🐛 **DEBUGGING GUIDE: FIR Severity Not Updating on Blockchain**

## 🔍 **ISSUE ANALYSIS**

The severity calculated by AI was not being properly stored on the blockchain due to:

1. **Double AI Calls**: Both frontend and blockchain backend were calling AI service
2. **Severity Override**: Blockchain backend was overriding frontend's calculated severity
3. **Missing Error Handling**: AI failures weren't being properly logged

## ✅ **FIXES IMPLEMENTED**

### **1. Updated Blockchain Backend Logic**
```javascript
// Now uses severity from frontend (already calculated by AI)
let severity = firData.severity || 1;

// Only calls AI if severity is not provided by frontend
if (!firData.severity) {
    // Calculate using AI as fallback
}
```

### **2. Enhanced Logging**
```javascript
console.log('Using severity from frontend:', severity);
console.log('Final severity for blockchain:', severity);
console.log('Transaction mined with severity:', severity);
```

### **3. Improved Frontend Error Handling**
```javascript
// Better error handling and default values
if (priority === 'high') {
    severity = 3;
} else if (priority === 'medium') {
    severity = 2;
} else {
    severity = 1; // Default for 'low' or any other case
}
```

## 🧪 **TESTING THE FIX**

### **Test 1: Check AI Service**
```bash
curl -X POST http://localhost:5050/classify \
  -H "Content-Type: application/json" \
  -d '{"incidentDescription": "Someone stole my phone and wallet"}'

# Expected Response:
# {"priority": "medium"}  → Should result in severity = 2
```

### **Test 2: Check Frontend to Blockchain Flow**
1. **Open browser developer console**
2. **File a FIR with description**: "Armed robbery at gunpoint"
3. **Check console logs for**:
   ```
   AI Raw Response: {priority: "high"}
   Parsed priority: high
   Final severity calculated: 3
   Saving FIR locally: {severity: 3, ...}
   ```

### **Test 3: Verify Blockchain Transaction**
```bash
# Check blockchain backend logs
tail -f /var/log/supervisor/blockchainbackend.*.log

# Look for:
# Using severity from frontend: 3
# Final severity for blockchain: 3
# Transaction mined with severity: 3
```

## 🔧 **DEBUGGING STEPS**

### **Step 1: Verify AI Service Response**
```bash
# Test with different crime types
curl -X POST http://localhost:5050/classify \
  -H "Content-Type: application/json" \
  -d '{"incidentDescription": "Murder case"}'  # Should return "high"

curl -X POST http://localhost:5050/classify \
  -H "Content-Type: application/json" \
  -d '{"incidentDescription": "Lost wallet"}'  # Should return "low"
```

### **Step 2: Check Frontend AI Integration**
1. Open **browser developer console** (F12)
2. Go to **Network tab**
3. File a FIR and check:
   - AI service call to `/classify`
   - Response contains `{"priority": "high/medium/low"}`
   - Console logs show correct severity calculation

### **Step 3: Verify Blockchain Backend**
```bash
# Check blockchain backend logs
cat /var/log/supervisor/blockchainbackend.*.log | grep -i severity

# Should show:
# Using severity from frontend: [1/2/3]
# Final severity for blockchain: [1/2/3]
```

### **Step 4: Verify Smart Contract Transaction**
1. Check the transaction hash in **Etherscan** (Sepolia testnet)
2. Look at the transaction **logs/events**
3. Verify **FIRCreated** event contains correct severity

## 🎯 **SEVERITY MAPPING REFERENCE**

| AI Priority | Severity Value | Crime Examples |
|-------------|---------------|----------------|
| **"high"** | **3** | Murder, rape, terrorism, bomb threats |
| **"medium"** | **2** | Robbery, theft, fraud, hacking |
| **"low"** | **1** | Lost items, noise complaints, littering |

## 🚨 **COMMON ISSUES & SOLUTIONS**

### **Issue 1: AI Service Returns Error**
**Symptoms**: Severity always shows as 1
**Solution**: 
```bash
# Check AI service logs
tail -f /var/log/supervisor/ai.*.log

# Check GROQ API key is valid
echo $GROQ_API_KEY
```

### **Issue 2: Frontend Not Calling AI**
**Symptoms**: No AI network request in browser
**Solution**:
```javascript
// Check environment variable
console.log(process.env.REACT_APP_AI_SERVICE_URL);

// Verify CORS settings in AI service
```

### **Issue 3: Blockchain Transaction Fails**
**Symptoms**: Transaction hash not generated
**Solution**:
```bash
# Check blockchain backend logs for gas/network errors
# Verify contract address and private key
# Check Ethereum network connection
```

### **Issue 4: Severity Not Stored in Contract**
**Symptoms**: Transaction succeeds but severity wrong
**Solution**:
```solidity
// Verify smart contract createFIR function
// Check if severity parameter is correctly handled
// Verify ABI matches contract function
```

## 🔍 **MONITORING & VERIFICATION**

### **Real-time Monitoring**
```bash
# Watch all service logs simultaneously
tail -f /var/log/supervisor/*.log | grep -i severity

# Monitor specific service
tail -f /var/log/supervisor/blockchainbackend.*.log
```

### **End-to-End Verification**
1. **File FIR** with high-priority crime description
2. **Check browser console** for severity calculation
3. **Verify blockchain logs** show correct severity
4. **Check transaction** on Etherscan for correct event data
5. **Confirm IPFS data** includes correct severity

## ✅ **SUCCESS CRITERIA**

The fix is working correctly when:
- [ ] ✅ AI service returns consistent priority classifications
- [ ] ✅ Frontend correctly maps priority to severity (1/2/3)
- [ ] ✅ Blockchain backend uses frontend's calculated severity
- [ ] ✅ Smart contract transaction includes correct severity
- [ ] ✅ IPFS data contains the calculated severity
- [ ] ✅ Blockchain logs show severity propagation throughout the flow

## 🎉 **FIXED FLOW**

```
User Input → Frontend AI Call → Calculate Severity → Send to Blockchain → Store with Correct Severity
     ↓              ↓                    ↓                ↓                      ↓
"Armed robbery" → priority:"high" → severity:3 → blockchain:3 → contract:severity=3
```

The severity should now be properly calculated by AI and stored on the blockchain with the correct value!