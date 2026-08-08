from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "DevOps CI/CD Project is running!",
        "status": "success"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/api/users")
def users():
    return jsonify([
        {"id": 1, "name": "Akash"},
        {"id": 2, "name": "DevOps User"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)