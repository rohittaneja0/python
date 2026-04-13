# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
from uuid import uuid4

app = Flask(__name__)
CORS(app)

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(load_tasks())

@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json() or {}
    title = data.get("title", "").strip()
    if not title:
        return jsonify({"error": "Title is required"}), 400

    tasks = load_tasks()
    task = {"id": str(uuid4()), "title": title, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    return jsonify(task), 201

@app.route("/api/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json() or {}
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            if "title" in data:
                task["title"] = data["title"]
            if "completed" in data:
                task["completed"] = bool(data["completed"])
            save_tasks(tasks)
            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404

@app.route("/api/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()
    updated = [t for t in tasks if t["id"] != task_id]
    if len(updated) == len(tasks):
        return jsonify({"error": "Task not found"}), 404
    save_tasks(updated)
    return "", 204

if __name__ == "__main__":
    app.run(port=5001, debug=True)