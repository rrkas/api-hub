from flask import Blueprint, request

from app.config import conf

main_bp = Blueprint("main_bp", __name__)


@main_bp.route("/")
def home():
    return {
        "name": conf.NAME,
        "creator": conf.CREATOR,
        "version": conf.VERSION,
        "endpoints": conf.PROG_ENDPOINTS,
    }


# ===================== error ==========================


@main_bp.app_errorhandler(404)
def err_404(err):
    return {
        "error-code": 404,
        "possible-solution": "Check request/route again",
        "message": "Page Not Found!",
        "full path": request.full_path,
        "path": request.path,
    }


@main_bp.app_errorhandler(405)
def err_405(err):
    return {
        "error-code": 405,
        "possible-solution": "Check request method!",
        "message": "Method Not Allowed!",
        "url": request.url,
        "method-used": request.method,
    }


@main_bp.app_errorhandler(500)
def err_500(err):
    return {
        "error-code": 500,
        "possible-solution": "Retry after some time!",
        "message": "Server error!",
    }
