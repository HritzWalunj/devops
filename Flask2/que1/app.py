from flask import Flask, jsonify
import json

app = Flask(__name__)

FILE="data.json"

@app.route("/api",methods=['GET'])
def get_data():
    try:
        with open(FILE,"r") as file:
            data = json.load(file)
            file.close()
            return jsonify(data)
    except FileNotFoundError:
        return jsonify({"Error":"File Not Found"})


if __name__ == "__main__":
    app.run(debug=True)
