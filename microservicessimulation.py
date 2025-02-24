# 3. BASIC MICROSERVICES SIMULATION USING FLASK
# Simulates service-to-service communication in a microservices architecture.

# Note: This requires Flask. Install with: pip install flask

from flask import Flask, jsonify

# User Service
user_service = Flask('user_service')

@user_service.route('/user/<username>')
def get_user(username):
    return jsonify({"username": username, "role": "admin"})

# Order Service
order_service = Flask('order_service')

@order_service.route('/order/<order_id>')
def get_order(order_id):
    return jsonify({"order_id": order_id, "status": "confirmed"})


# To run these microservices:
# 1. Save each service in a separate Python file.
# 2. Run with: flask run --port=<port_number>
# Example: flask run --port=5000 for user_service, flask run --port=5001 for order_service
# 3. Use Postman or browser to access endpoints.

# Example API Calls:
# http://localhost:5000/user/john_doe
# http://localhost:5001/order/12345