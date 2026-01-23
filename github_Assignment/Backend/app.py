from flask import Flask, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__main__)

MONGO_URI=os.getenv("MONGODB_ATLAS_CONNECTION_STRING")
client = MongoClient(MONGO_URI)
db = client.items_info
collection = db.items

@app.route("/submittodoitem", methods=['POST'])
def get_items():
    item_name = request.form("Item_name")
    item_details = request.form("ItemDescription")

    if not item_name or item_details:
        return jsonify({"Error": "Missing Field"}), 400

    to_do_item = {
        "item_name" : item_name ,
        "item_details" : item_details
    }
    
    collection.insert_one(to_do_item)
  return jsonify({"message": "To-Do item saved successfully"}), 201

  if __name__ == "__main__":
    app.run(debug=True)
