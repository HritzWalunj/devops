from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json or request.form

    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and Email are required"}), 400

    # Simulating successful processing
    print("Received Data:", data)

    return jsonify({"message": "Success"}), 200

app.run(host="0.0.0.0", port=5000)
