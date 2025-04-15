from flask import Blueprint, jsonify
from pymongo import MongoClient
from bson import ObjectId

# Setup MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["twitter_trends"]
collection = db["trends_by_hour"]

# Flask Blueprint
trends_blueprint = Blueprint('trends_api', __name__, url_prefix='/api')

# JSON encoder for ObjectId
def convert_objid(data):
    for item in data:
        item["_id"] = str(item["_id"])
    return data

# /api/trends
@trends_blueprint.route('/trends')
def get_trends():
    data = list(collection.find().sort("timestamp", -1).limit(24))
    return jsonify(convert_objid(data))
