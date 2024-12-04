<template>
  <div class="api-table">
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
        <tr v-for="(log, index) in parsedLogs" :key="index">
          <td>{{ log.apiName }}</td>
          <td>{{ log.time }}</td>
          <td>{{ log.httpCode }}</td>
          <td>
            <span
              :class="log.status === 'Success' ? 'status-success' : 'status-fail'"
            ></span>
          </td>
          <td>expert@gmail.com</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { fetchMonitoringResults } from '@/services/apiService';

export default {
  data() {
    return {
      logs: [],
    };
  },
  computed: {
    parsedLogs() {
      return this.logs.map(log => {
        const parts = log.split(' - ');
        const status = parts[3]?.includes('Success') ? 'Success' : 'Failure';
        return {
          apiName: parts[2]?.split(':')[1]?.trim(),
          time: parts[0]?.trim(),
          httpCode: status === 'Success' ? 200 : 'Error',
          status,
        };
      });
    },
  },
  async created() {
    try {
      this.logs = await fetchMonitoringResults();
    } catch (error) {
      console.error('Failed to load monitoring results', error);
    }
  },
};
</script>

<style scoped>
.status-success {
  display: inline-block;
  width: 12px;
  height: 12px;
  background-color: green;
  border-radius: 50%;
}

.status-fail {
  display: inline-block;
  width: 12px;
  height: 12px;
  background-color: red;
  border-radius: 50%;
}
</style>
