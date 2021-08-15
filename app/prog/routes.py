from flask import Blueprint, request

from app.prog.algos import *
from app.prog.theory import ProgTheory

prog_bp = Blueprint("prog_bp", __name__)

prog_root = "/prog"

PROG_ENDPOINTS = [
    "infix-to-prefix",
    "infix-to-postfix",
]
PROG_DETAILED_ENDPOINTS = ["<endpoint>/theory"]


@prog_bp.route(prog_root)
def prog_home():
    return {
        "api-name": "prog",
        "purpose": "algos and conversions",
        "endpoints": PROG_ENDPOINTS,
        "endpoints-detailed": PROG_DETAILED_ENDPOINTS,
    }


@prog_bp.route(prog_root + "/infix-to-prefix", methods=["GET", "POST"])
def prog_infix_to_prefix():
    if request.method == "POST":
        expr_key = "expr"
        if (
            expr_key not in request.form.keys()
            and expr_key not in (request.json or {}).keys()
        ):
            return {"error": f"{expr_key} missing in body!"}
        if expr_key in request.form.keys():
            expr = request.form.get(expr_key)
        else:
            expr = request.json[expr_key]
        res = infix_to_prefix(expr)
        return {"result": res}
    return {
        "api-name": "infix-to-prefix",
        "methods": ["GET", "POST"],
        "sample request": {
            "method": "POST",
            "url": request.base_url,
            "headers": {"Content-Type": "application/json"},
            "body": {"expr": "( a + b ) ^ c"},
        },
    }


@prog_bp.route(prog_root + "/infix-to-postfix", methods=["GET", "POST"])
def prog_infix_to_postfix():
    if request.method == "POST":
        expr_key = "expr"
        if (
            expr_key not in request.form.keys()
            and expr_key not in (request.json or {}).keys()
        ):
            return {"error": f"{expr_key} missing in body!"}
        if expr_key in request.form.keys():
            expr = request.form.get(expr_key)
        else:
            expr = request.json[expr_key]
        res = infix_to_postfix(expr)
        return {"result": res}
    return {
        "api-name": "infix-to-postfix",
        "methods": ["GET", "POST"],
        "sample request": {
            "method": "POST",
            "url": request.base_url,
            "headers": {"Content-Type": "application/json"},
            "body": {"expr": "( a + b ) ^ c"},
        },
    }


@prog_bp.route(prog_root + "/<string:algo>/theory")
def prog_theory(algo):
    t = ProgTheory.find_algo_by_route(algo)
    if t:
        return t.route_info()
    else:
        return {"error": "algo not found"}
