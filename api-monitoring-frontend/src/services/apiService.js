import axios from "axios";

const BASE_URL = "http://localhost:5000";

export async function fetchMonitoringResults() {
  try {
    const response = await axios.get(`${BASE_URL}/api/monitoring-results`);
    return response.data.logs; // Return the logs array directly
  } catch (error) {
    console.error("Error fetching monitoring results:", error);
    throw error;
  }
}
