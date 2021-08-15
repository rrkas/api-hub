from flask import Blueprint

from app import conf

cetb_bp = Blueprint("cetb_bp", __name__)

endpoints = {}


@cetb_bp.route("/cetb")
def cetb_home():
    data = {
        "api_name": f"{conf.NAME}.cetb",
        "endpoints": endpoints,
        "source_url": "https://cet.edu.in/",
        "status": "incomplete",
    }
    return data
