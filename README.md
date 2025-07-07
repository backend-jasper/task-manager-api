# ✅ Task Manager API (Flask)

A simple RESTful API for managing user tasks, built with **Flask** and Python. Ideal for learning, local testing, or as a starter project for backend development.

---

## 🚀 Features

- 🔐 Register new users (`username`, `password`)
- 🔑 Login existing users
- 📝 Add tasks to a user account
- 📋 View all tasks for a specific user
- 💾 Data stored in a JSON file (simple mock database)

---

## 🛠️ How to Use (with `curl`)

### ➕ Register a User
```bash
curl -X POST http://127.0.0.1:5000/register \
  -H "Content-Type: application/json" \
  -d '{"username":"test", "password":"123"}'


### LOGIN USER
curl -X POST http://127.0.0.1:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username":"test", "password":"123"}'

### Add Task
curl -X POST http://127.0.0.1:5000/add-task \
  -H "Content-Type: application/json" \
  -d '{"username":"test", "task":"Finish the report"}'

### View Tasks for a users
curl http://127.0.0.1:5000/tasks/test

⚙ Technologies Used

 Python

 Flask

 JSON (for lightweight data storage)

 Termux(android)(for mobile development)

🧑‍💻 Author

DefSoledad
Backend Developer in Training — Passionate about building simple, clean, and effective backend systems.



