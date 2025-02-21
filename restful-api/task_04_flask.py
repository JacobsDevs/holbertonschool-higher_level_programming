#!/usr/bin/python3
from flask import Flask, jsonify, request
import json

app = Flask(__name__)
users = {}
@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def user(username):
    if username in users.keys():
        return jsonify(users[username])
    else:
        return {"error": "User not found"}

@app.route("/add_user", methods=['POST'])
def add_user():
    user_info = json.loads(request.data)
    if all(x in user_info.keys() for x in ['username', 'age', 'name', 'city']):
        users[user_info['username']] = user_info
    else:
        return {"error": "Username is required"}, 400
    response = {"message": "User added", "user": user_info}
    return jsonify(response), 201

if __name__ == "__main__":
    app.run()
