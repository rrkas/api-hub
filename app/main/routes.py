import os

import pyperclip
from flask import Blueprint, request, render_template, send_file, current_app, flash

from app.main.documentation import get_docs, find_doc_with_id
from app.util import request_info

main_bp = Blueprint("main_bp", __name__)


@main_bp.route("/")
def home():
    data = request_info(request)
    docs = get_docs()
    return render_template(
        "index.html", req=request_info(request), data=data, docs=docs
    )


@main_bp.route("/favicon.ico")
def favicon():
    return send_file(os.path.join(current_app.static_folder, "apihub.png"))


@main_bp.route("/copy/<string:html_id>")
def copy_py_code(html_id):
    doc = find_doc_with_id(html_id)
    if doc:
        pyperclip.copy(doc.py_code)
        return doc.name
    return ''


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
