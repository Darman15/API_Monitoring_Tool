<template>
    <div class="api-monitor-table">
      <h2>API Monitoring Results</h2>
      <table>
  <thead>
    <tr>
      <th>API Name</th>
      <th>Last Test Time</th>
      <th>HTTP Code</th>
      <th>Status</th>
      <th>SME</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="result in apiResults" :key="result.apiName">
      <td>{{ result.apiName }}</td>
      <td>{{ result.lastTestTime }}</td>
      <td>{{ result.statusCode }}</td>
      <td>
        <span :style="{ backgroundColor: result.status, borderRadius: '50%', padding: '5px', color: 'white', display: 'inline-block' }">
          &nbsp;&nbsp;
        </span>
      </td>
      <td>{{ result.sme }}</td>
    </tr>
  </tbody>
</table>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        apiResults: [],
      };
    },
    methods: {
        async fetchApiData() {
    try {
      console.log('Fetching data from Flask server...');
      const response = await axios.get('http://localhost:5000/api/monitoring-results');
      console.log('Response received:', response.data);
      
      // Parse logs and extract details
      this.apiResults = response.data.logs.map(log => {
        const logParts = log.match(/API (\w+): (\w+) with status code (\d+)/);
        if (logParts) {
          return {
            apiName: logParts[1],
            status: logParts[2] === 'Success' ? 'green' : 'red',
            statusCode: logParts[3],
            lastTestTime: log.split(' - ')[0],
            sme: 'expert@gmail.com'
          };
        }
        return null;
      }).filter(entry => entry !== null);
      
    } catch (error) {
      console.error('Error fetching API data:', error);
      alert('Failed to fetch API data. Check the console for details.');
        }
      },
    },
    mounted() {
      this.fetchApiData();
    }
  };
  </script>
  
  <style scoped>
  .api-monitor-table {
    padding: 20px;
    background-color: #f7faff;
    border-radius: 10px;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th, td {
    padding: 10px;
    text-align: left;
  }
  
  .status-indicator {
    display: inline-block;
    width: 15px;
    height: 15px;
    border-radius: 50%;
  }
  
  .success {
    background-color: green;
    box-shadow: 0 0 10px green;
  }
  
  .failure {
    background-color: red;
    box-shadow: 0 0 10px red;
  }
  </style>
  