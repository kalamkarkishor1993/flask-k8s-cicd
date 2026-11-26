from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello from my pipeline")

@app.route("/health")
def health():
    return jsonify(status="ok"), 200
