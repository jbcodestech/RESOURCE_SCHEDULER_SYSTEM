from flask import Flask, jsonify
import random

app = Flask(__name__)

# Sample agents
agents = [
    {"id": 1, "name": "Agent A", "status": "available"},
    {"id": 2, "name": "Agent B", "status": "available"},
]

# Sample customer requests
customer_requests = [
    {"id": 1, "type": "VIP", "service_time": random.randint(5, 15)},
    {"id": 2, "type": "Normal", "service_time": random.randint(5, 15)},
]

@app.route('/schedule', methods=['GET'])
def schedule():
    # Assign an available agent to the next request
    for agent in agents:
        if agent["status"] == "available":
            task = customer_requests.pop(0) if customer_requests else None
            if task:
                agent["status"] = "busy"
                return jsonify({"agent": agent, "task": task})
            else:
                return jsonify({"message": "No tasks available"})
    return jsonify({"message": "No agents available"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
