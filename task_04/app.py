from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

# GET single user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# POST - create a new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Name and email required"}), 400

    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = {"name": data["name"], "email": data["email"]}
    return jsonify({"id": new_id, "message": "User created"}), 201

# PUT - update user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    if not data:
        return jsonify({"error": "No data provided"}), 400

    users[user_id].update(data)
    return jsonify({"message": "User updated"}), 200

# DELETE - remove user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
