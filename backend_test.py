import requests
import sys
import os
from datetime import datetime
import json
import time

class JusticeChainAPITester:
    def __init__(self, base_url="http://localhost:5000", blockchain_url="http://localhost:4000"):
        self.base_url = base_url
        self.blockchain_url = blockchain_url
        self.tests_run = 0
        self.tests_passed = 0

    def run_test(self, name, method, endpoint, expected_status, data=None, base="main", expect_json=True):
        """Run a single API test"""
        url = f"{self.base_url}/{endpoint}" if base == "main" else f"{self.blockchain_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}
        
        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        print(f"URL: {url}")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers)

            success = response.status_code == expected_status
            
            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                
                if expect_json:
                    response_data = response.json()
                    # Print a truncated version of the response if it's too large
                    if isinstance(response_data, dict) and 'data' in response_data and isinstance(response_data['data'], list) and len(response_data['data']) > 2:
                        truncated_data = response_data.copy()
                        truncated_data['data'] = [response_data['data'][0], "... truncated ..."]
                        print(f"Response (truncated): {json.dumps(truncated_data, indent=2)}")
                    else:
                        print(f"Response: {json.dumps(response_data, indent=2)}")
                else:
                    print(f"Response: {response.text}")
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                print(f"Response: {response.text}")

            if expect_json:
                return success, response.json() if response.status_code < 400 else {}
            else:
                return success, response.text if response.status_code < 400 else ""

        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            return False, {} if expect_json else ""

    def test_citizen_login(self, email, password):
        """Test citizen login"""
        return self.run_test(
            "Citizen Login",
            "POST",
            "api/auth/citizen/login",
            200,
            data={"email": email, "password": password}
        )

    def test_admin_login(self, email, password):
        """Test admin login"""
        return self.run_test(
            "Admin Login",
            "POST",
            "api/auth/admin/login",
            200,
            data={"email": email, "password": password}
        )
        
    def test_blockchain_health(self):
        """Test blockchain backend health endpoint"""
        return self.run_test(
            "Blockchain Backend Health",
            "GET",
            "",
            200,
            base="blockchain",
            expect_json=False
        )
        
    def test_get_all_firs(self):
        """Test getting all FIRs from blockchain/Pinata"""
        return self.run_test(
            "Get All FIRs from Blockchain/Pinata",
            "GET",
            "api/getAllFIRs",
            200,
            base="blockchain"
        )
        
    def test_search_fir(self, search_type, search_value):
        """Test searching FIR by type and value"""
        return self.run_test(
            f"Search FIR by {search_type}: {search_value}",
            "POST",
            "api/searchFIR",
            200,
            data={"searchType": search_type, "searchValue": search_value},
            base="blockchain"
        )
        
    def test_get_fir_by_id(self, fir_id):
        """Test getting a specific FIR by ID"""
        return self.run_test(
            f"Get FIR by ID: {fir_id}",
            "GET",
            f"api/getFIR/{fir_id}",
            200,
            base="blockchain"
        )

def main():
    # Get environment variables for URLs
    frontend_env = {}
    try:
        with open('/app/frontend/.env', 'r') as f:
            for line in f:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    frontend_env[key] = value
    except Exception as e:
        print(f"Error reading frontend .env file: {e}")
    
    # Use environment variables if available, otherwise use defaults
    backend_url = frontend_env.get('REACT_APP_BACKEND_URL', 'http://localhost:5000')
    blockchain_url = frontend_env.get('REACT_APP_BLOCKCHAIN_BACKEND_URL', 'http://localhost:4000')
    
    print(f"Using Backend URL: {backend_url}")
    print(f"Using Blockchain Backend URL: {blockchain_url}")
    
    # Setup
    tester = JusticeChainAPITester(backend_url, blockchain_url)
    
    # Test blockchain backend health
    print("\n===== Testing Blockchain Backend Health =====")
    blockchain_health, health_data = tester.test_blockchain_health()
    
    if not blockchain_health:
        print("❌ Blockchain backend is not available. Skipping blockchain tests.")
        return 1
        
    # Test getting all FIRs from blockchain/Pinata
    print("\n===== Testing Get All FIRs from Blockchain/Pinata =====")
    all_firs_success, all_firs_data = tester.test_get_all_firs()
    
    # Extract a FIR ID for further testing if available
    fir_id = None
    fir_number = None
    email = None
    phone = None
    id_number = None
    
    if all_firs_success and 'data' in all_firs_data and all_firs_data['data']:
        # Get the first FIR data
        first_fir = all_firs_data['data'][0]
        fir_id = first_fir.get('id')
        fir_number = first_fir.get('firNumber')
        email = first_fir.get('email')
        phone = first_fir.get('phone')
        id_number = first_fir.get('idNumber')
        
        print(f"Found FIR data for testing:")
        print(f"  - ID: {fir_id}")
        print(f"  - FIR Number: {fir_number}")
        print(f"  - Email: {email}")
        print(f"  - Phone: {phone}")
        print(f"  - ID Number: {id_number}")
        
        # Add a delay to avoid rate limiting
        print("\nWaiting 2 seconds to avoid rate limiting...")
        time.sleep(2)
        
        # Test search by FIR number if available
        if fir_number:
            print("\n===== Testing Search FIR by FIR Number =====")
            tester.test_search_fir('fir', fir_number)
            time.sleep(1)  # Add delay between requests
            
        # Test search by phone if available
        if phone:
            print("\n===== Testing Search FIR by Phone =====")
            tester.test_search_fir('phone', phone)
            time.sleep(1)  # Add delay between requests
            
        # Test search by email if available
        if email:
            print("\n===== Testing Search FIR by Email =====")
            tester.test_search_fir('email', email)
            time.sleep(1)  # Add delay between requests
            
        # Test search by ID number if available
        if id_number:
            print("\n===== Testing Search FIR by ID Number =====")
            tester.test_search_fir('id', id_number)
            time.sleep(1)  # Add delay between requests
            
        # Test getting a specific FIR by ID
        print(f"\n===== Testing Get FIR by ID =====")
        tester.test_get_fir_by_id(fir_id)
    else:
        print("No FIRs found in blockchain/Pinata. Testing with sample values.")
        
        # Test search with sample values
        print("\n===== Testing Search FIR by FIR Number (Sample) =====")
        tester.test_search_fir('fir', 'FIR2025')
        time.sleep(1)  # Add delay between requests
        
        # Test get FIR by ID with sample value
        print("\n===== Testing Get FIR by ID (Sample) =====")
        tester.test_get_fir_by_id('1')
    
    # Print results
    print(f"\n📊 Tests passed: {tester.tests_passed}/{tester.tests_run}")
    
    if tester.tests_passed == tester.tests_run:
        print("✅ All blockchain backend API endpoints are working correctly")
    else:
        print("❌ Some blockchain backend API tests failed")
        print("Note: Some failures may be due to Pinata API rate limiting (429 errors)")
    
    return 0 if tester.tests_passed == tester.tests_run else 1

if __name__ == "__main__":
    sys.exit(main())