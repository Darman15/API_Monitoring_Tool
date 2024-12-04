from flask import Flask, jsonify
import os
from datetime import datetime
from flask_cors import CORS  # Add this import

app = Flask(__name__)
CORS(app)

LOGS_DIR = 'logs'

def get_latest_log_content():
    try:
        today = datetime.now().strftime('%Y-%m-%d')
        log_filename = f"{LOGS_DIR}/{today}.log"
        
        # Check if the log file exists
        if not os.path.exists(log_filename):
            return None

        # Read the log file
        with open(log_filename, 'r') as file:
            return file.readlines()

    except Exception as e:
        print(f"Error reading log file: {str(e)}")
        return None

@app.route('/api/monitoring-results', methods=['GET'])
def get_monitoring_results():
    log_content = get_latest_log_content()
    if log_content is None:
        return jsonify({"error": "Failed to fetch logs"}), 500
    
    return jsonify({"logs": log_content}), 200

if __name__ == '__main__':
    app.run(debug=True)
