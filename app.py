from flask import Flask, jsonify
import redis

app = Flask(__name__)

cache = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)


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


@app.route("/visits")
def visits():
    count = cache.incr("visits")

    return jsonify({
        "visits": count
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)