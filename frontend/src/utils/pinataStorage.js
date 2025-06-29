// Pinata/Blockchain storage utility for managing FIR data
const BLOCKCHAIN_BACKEND_URL = process.env.REACT_APP_BLOCKCHAIN_BACKEND_URL || 'http://localhost:4000';

export class PinataStorage {
  // Get all FIRs from Pinata via blockchain backend
  static async getAllFIRs() {
    try {
      console.log('Fetching all FIRs from Pinata storage...');
      
      const response = await fetch(`${BLOCKCHAIN_BACKEND_URL}/api/getAllFIRs`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();
      
      if (result.success) {
        console.log(`Successfully retrieved ${result.data.length} FIRs from Pinata`);
        return result.data;
      } else {
        throw new Error(result.message || 'Failed to fetch FIRs from Pinata');
      }
    } catch (error) {
      console.error('Error fetching FIRs from Pinata:', error);
      // Fallback to localStorage if Pinata fails
      console.log('Falling back to localStorage...');
      const localData = localStorage.getItem('justice_chain_firs');
      return localData ? JSON.parse(localData) : [];
    }
  }

  // Search FIR by various criteria from Pinata
  static async searchFIR(searchType, searchValue) {
    try {
      console.log('Searching FIR in Pinata:', searchType, searchValue);
      
      const response = await fetch(`${BLOCKCHAIN_BACKEND_URL}/api/searchFIR`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          searchType,
          searchValue
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();
      
      if (result.success) {
        return result.data;
      } else {
        throw new Error(result.message || 'Failed to search FIR in Pinata');
      }
    } catch (error) {
      console.error('Error searching FIR in Pinata:', error);
      // Fallback to localStorage search
      console.log('Falling back to localStorage search...');
      const localData = localStorage.getItem('justice_chain_firs');
      if (!localData) return null;
      
      const allFIRs = JSON.parse(localData);
      const searchValueLower = searchValue.toLowerCase().trim();
      
      const result = allFIRs.find(fir => {
        switch (searchType) {
          case 'fir':
            return fir.firNumber.toLowerCase().includes(searchValueLower);
          case 'phone':
            return fir.phone && fir.phone.includes(searchValue);
          case 'email':
            return fir.email && fir.email.toLowerCase().includes(searchValueLower);
          case 'id':
            return fir.idNumber && fir.idNumber.toLowerCase().includes(searchValueLower);
          default:
            return false;
        }
      });

      return result || null;
    }
  }

  // Get specific FIR by ID from Pinata
  static async getFIRById(id) {
    try {
      console.log('Fetching FIR by ID from Pinata:', id);
      
      const response = await fetch(`${BLOCKCHAIN_BACKEND_URL}/api/getFIR/${id}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();
      
      if (result.success) {
        return result.data;
      } else {
        throw new Error(result.message || 'Failed to fetch FIR from Pinata');
      }
    } catch (error) {
      console.error('Error fetching FIR by ID from Pinata:', error);
      // Fallback to localStorage
      const localData = localStorage.getItem('justice_chain_firs');
      if (!localData) return null;
      
      const allFIRs = JSON.parse(localData);
      return allFIRs.find(fir => fir.id === id || fir.blockchainId === parseInt(id)) || null;
    }
  }

  // Get FIR statistics from Pinata data
  static async getStatistics() {
    try {
      const allFIRs = await this.getAllFIRs();
      const total = allFIRs.length;
      const statuses = allFIRs.reduce((acc, fir) => {
        acc[fir.status] = (acc[fir.status] || 0) + 1;
        return acc;
      }, {});

      return {
        total,
        registered: statuses['FIR Registered'] || 0,
        underInvestigation: statuses['Under Investigation'] || 0,
        resolved: statuses['Case Closed'] || 0,
        pending: statuses['Pending'] || 0
      };
    } catch (error) {
      console.error('Error getting statistics from Pinata:', error);
      return { total: 0, registered: 0, underInvestigation: 0, resolved: 0, pending: 0 };
    }
  }

  // Update FIR status (this would require blockchain transaction)
  static async updateFIRStatus(firNumber, newStatus, description, officer = 'Admin') {
    try {
      // Note: In a real implementation, this would require a blockchain transaction
      // For now, we'll update localStorage as fallback and notify about limitation
      console.warn('Status update on blockchain not implemented yet, updating localStorage only');
      
      const localData = localStorage.getItem('justice_chain_firs');
      if (!localData) {
        return { success: false, error: 'No local data found' };
      }

      const allFIRs = JSON.parse(localData);
      const firIndex = allFIRs.findIndex(fir => fir.firNumber === firNumber);
      
      if (firIndex === -1) {
        return { success: false, error: 'FIR not found' };
      }

      const updatedFIR = { ...allFIRs[firIndex] };
      updatedFIR.status = newStatus;
      updatedFIR.lastUpdated = new Date().toISOString().split('T')[0];
      
      // Add timeline entry
      if (!updatedFIR.timeline) updatedFIR.timeline = [];
      updatedFIR.timeline.push({
        date: new Date().toISOString().split('T')[0],
        status: newStatus,
        description: description,
        officer: officer
      });

      allFIRs[firIndex] = updatedFIR;
      localStorage.setItem('justice_chain_firs', JSON.stringify(allFIRs));
      
      return { success: true };
    } catch (error) {
      console.error('Error updating FIR status:', error);
      return { success: false, error: error.message };
    }
  }

  // Check if blockchain backend is available
  static async isBlockchainAvailable() {
    try {
      const response = await fetch(`${BLOCKCHAIN_BACKEND_URL}/`, {
        method: 'GET',
        timeout: 5000
      });
      return response.ok;
    } catch (error) {
      console.log('Blockchain backend not available:', error.message);
      return false;
    }
  }
}