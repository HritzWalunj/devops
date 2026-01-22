from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Read MongoDB URI from .env
MONGO_URI = os.getenv("MONGODB_ATLAS_CONNECTION_STRING")

# MongoDB Atlas connection
client = MongoClient(MONGO_URI)
db = client.testdb
collection = db.users

@app.route("/", methods=["GET", "POST"])
def form():
    error = None

    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]
            confirm_password = request.form["comform password"]

            collection.insert_one({
                "name": name,
                "email": email,
                "password":password,
                "confirm_password":confirm_password
            })

            return redirect(url_for("success"))

        except Exception as e:
            error = str(e)

    return render_template("login.html", error=error)


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
