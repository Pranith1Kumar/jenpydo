# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Basic Calculator API"

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    return jsonify({"result": data["a"] + data["b"]})

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.json
    return jsonify({"result": data["a"] - data["b"]})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.json
    return jsonify({"result": data["a"] * data["b"]})

@app.route('/divide', methods=['POST'])
def divide():
    data = request.json
    if data["b"] == 0:
        return jsonify({"error": "Division by zero is not allowed"})
    return jsonify({"result": data["a"] / data["b"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
