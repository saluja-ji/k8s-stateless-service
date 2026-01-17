from flask import Flask, jsonify
import os
import time

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

@app.route("/")
def home():
    return jsonify(
        service="k8s-prod-blueprint",
        environment=os.getenv("ENV", "unknown")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
