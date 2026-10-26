import os
from flask import Flask, jsonify

app = Flask(__name__)

# Read environment variable (defaults to "Development" if not set)
APP_ENV = os.environ.get("APP_ENV", "Development")

@app.route("/")
def home():
    return jsonify({
        "message": "CENG413 Containerization HW-1",
        "environment": APP_ENV
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    # Listen on port 8080 and host 0.0.0.0 inside the Docker container
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)