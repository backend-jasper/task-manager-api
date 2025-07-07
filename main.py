from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
FILENAME = "users.json"

# Load users from file
def load_users():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

# Save users to file
def save_users(users):
    with open(FILENAME, "w") as f:
        json.dump(users, f, indent=4)

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing fields"}), 400

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

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    users = load_users()
    for user in users:
        if user["username"] == data["username"] and user["password"] == data["password"]:
            return jsonify({"message": "Login successful", "user": user}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/add-task", methods=["POST"])
def add_task():
    data = request.get_json()
    if not data or "username" not in data or "task" not in data:
        return jsonify({"error": "Missing fields"}), 400

    users = load_users()
    for user in users:
        if user["username"] == data["username"]:
            user["tasks"].append(data["task"])
            save_users(users)
            return jsonify({"message": "Task added", "tasks": user["tasks"]}), 200
    return jsonify({"error": "User not found"}), 404

@app.route("/tasks/<username>", methods=["GET"])
def get_tasks(username):
    users = load_users()
    for user in users:
        if user["username"] == username:
            return jsonify({"tasks": user["tasks"]}), 200
    return jsonify({"error": "User not found"}), 404

# ✅ NEW DELETE-TASK ENDPOINT
@app.route("/delete-task", methods=["POST"])
def delete_task():
    data = request.get_json()
    if not data or "username" not in data or "task" not in data:
        return jsonify({"error": "Missing fields"}), 400

    users = load_users()
    for user in users:
        if user["username"] == data["username"]:
            if data["task"] in user["tasks"]:
                user["tasks"].remove(data["task"])
                save_users(users)
                return jsonify({"message": "Task deleted", "tasks": user["tasks"]}), 200
            else:
                return jsonify({"error": "Task not found"}), 404
    return jsonify({"error": "User not found"}), 404

# Server start
if __name__ == "__main__":
    app.run(debug=True)
