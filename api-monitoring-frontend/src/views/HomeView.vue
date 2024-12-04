<template>
  <div class="home">
    <h1>Welcome to the API Monitoring Tool</h1>
    <APIMonitorTable />
  </div>
</template>

<script>
import APIMonitorTable from '../components/APIMonitorTable.vue';

export default {
  name: 'HomeView',
  components: {
    APIMonitorTable
  }
};
</script>

<style scoped>
.home {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

h1 {
  color: #007bff;
  margin-bottom: 20px;
}
</style>

