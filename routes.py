from flask import Blueprint, request, jsonify
from utils import load_users, save_users

routes = Blueprint("routes", __name__)

@routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing username or password"}), 400

    users = load_users()
    for user in users:
        if user["username"] == data["username"]:
            return jsonify({"error": "Username already taken"}), 409

    new_user = {
        "username": data["username"],
        "password": data["password"],
        "tasks": []
    }
    users.append(new_user)
    save_users(users)
    return jsonify({"message": "User registered", "user": new_user}), 201


@routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    users = load_users()
    for user in users:
        if user["username"] == data["username"] and user["password"] == data["password"]:
            return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401


@routes.route("/add-task", methods=["POST"])
def add_task():
    data = request.get_json()
    users = load_users()
    for user in users:
        if user["username"] == data["username"]:
            user["tasks"].append(data["task"])
            save_users(users)
            return jsonify({"message": "Task added"}), 200
    return jsonify({"error": "User not found"}), 404


@routes.route("/tasks/<username>", methods=["GET"])
def view_tasks(username):
    users = load_users()
    for user in users:
        if user["username"] == username:
            return jsonify({"tasks": user["tasks"]}), 200
    return jsonify({"error": "User not found"}), 404
