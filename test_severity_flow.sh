#!/bin/bash

echo "🔍 Testing AI Severity Classification and Blockchain Integration"
echo "=============================================================="

# Test AI Service
echo "📡 Testing AI Service..."
AI_RESPONSE=$(curl -s -X POST http://localhost:5050/classify \
  -H "Content-Type: application/json" \
  -d '{"incidentDescription": "Someone broke into my house and stole valuable items"}')

echo "AI Response: $AI_RESPONSE"

# Extract priority from response
PRIORITY=$(echo $AI_RESPONSE | grep -o '"priority":"[^"]*"' | cut -d'"' -f4)
echo "Extracted Priority: $PRIORITY"

# Test severity mapping
case $PRIORITY in
  "high")
    EXPECTED_SEVERITY=3
    ;;
  "medium")
    EXPECTED_SEVERITY=2
    ;;
  "low")
    EXPECTED_SEVERITY=1
    ;;
  *)
    EXPECTED_SEVERITY=1
    ;;
esac

echo "Expected Severity for Blockchain: $EXPECTED_SEVERITY"

echo ""
echo "🔧 Testing Blockchain Backend..."

# Test blockchain backend with AI integration
BLOCKCHAIN_RESPONSE=$(curl -s -X POST http://localhost:4000/api/uploadFIR \
  -H "Content-Type: application/json" \
  -d '{
    "incidentType": "Theft/Burglary",
    "incidentDescription": "Someone broke into my house and stole valuable items",
    "incidentLocation": "Test Location",
    "fullName": "Test User",
    "severity": 2,
    "urgencyLevel": "medium"
  }')

echo "Blockchain Response: $BLOCKCHAIN_RESPONSE"

echo ""
echo "✅ Test completed!"
echo ""
echo "📋 Debugging Checklist:"
echo "1. Check AI service returns proper priority format"
echo "2. Verify frontend calculates severity correctly"
echo "3. Confirm blockchain backend uses frontend severity"
echo "4. Check smart contract accepts severity parameter"
echo "5. Verify transaction is mined successfully"
echo ""
echo "🎯 Expected Flow:"
echo "Frontend AI Call → Calculate Severity → Send to Blockchain → Store with Severity"