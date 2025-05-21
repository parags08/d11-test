There is no API and no backend changes. Only button color changed from Blue to Red

from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated database
users_db = {
    1: {"id": 1, "username": "alice", "email": "alice@example.com"},
    2: {"id": 2, "username": "bob", "email": "bob@example.com"},
    3: {"id": 3, "username": "charlie", "email": "charlie@example.com"}
}

# Simulated login (insecure, just by passing ?user_id=)
@app.before_request
def simulate_login():
    user_id = request.args.get("user_id")
    if user_id:
        request.user_id = int(user_id)
    else:
        request.user_id = None

# Vulnerable endpoint
@app.route("/profile/<int:profile_id>", methods=["GET"])
def get_profile(profile_id):
    # ⚠️ IDOR Vulnerability: No check if profile_id == request.user_id
    user = users_db.get(profile_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True)

// There is no API and no backend changes. Only button color changed from Blue to Red
