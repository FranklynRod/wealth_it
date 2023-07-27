from flask import Flask, jsonify, request, make_response, Blueprint
import requests
import os
from dotenv import load_dotenv
import requests
import json
from flask_cors import CORS


asset_bp = Blueprint("asset", __name__, url_prefix="/assets")

# CREATE asset entry
@asset_bp.route("/<asset_id>", strict_slashes=False, methods=["POST"])
def create_one_asset(asset_id):
    try:
        asset = get_validate(Asset, asset_id)
        request_body = 
    db.session.add()
    db.commit()
    return make_response(jsonify(),201)
    
# READ asset entry
@asset_bp.route("/<asset_id>", strict_slashes=False, methods=[""])
def read_one_asset(asset_id):


# DELETE asset entry
@asset_bp.route("/<asset_id>", strict_slashes=False, methods=["DELETE"])
def delete_one_asset(asset_id):

# Update asset entry
@asset_bp.route("/<asset_id>", strict_slashes=False, methods=["PUT"])
def update_one_asset(asset_id):
