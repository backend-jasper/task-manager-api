import json, os

FILENAME = "users.json"

def load_users():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    else:
        return []

def save_users(users):
    with open(FILENAME, "w") as f:
        json.dump(users, f, indent=4)
