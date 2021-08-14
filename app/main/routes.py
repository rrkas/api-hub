from flask import Blueprint, request

from app.config import conf

main_bp = Blueprint("main_bp", __name__)


@main_bp.route("/")
def home():
    data = {
        "name": conf.NAME,
        "creator": conf.CREATOR,
        "version": conf.VERSION,
        "endpoints": conf.ENDPOINTS,
    }
    return data


# ===================== error ==========================


@main_bp.app_errorhandler(404)
def err_404(err):
    data = {
        "error_code": 404,
        "possible solution": "Check request/route again",
        "message": "Page Not Found!",
        "full path": request.full_path,
        "path": request.path,
    }
    return data


@main_bp.app_errorhandler(500)
def err_500(err):
    data = {
        "error_code": 500,
        "possible solution": "Retry after some time!",
        "message": "Server error!",
    }
    return data
