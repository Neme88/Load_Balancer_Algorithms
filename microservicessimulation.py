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