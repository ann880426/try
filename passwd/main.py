from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello, Cloud Run!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
