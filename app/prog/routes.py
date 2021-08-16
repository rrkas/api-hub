from flask import Blueprint

from app.prog.theory import ProgTheory

prog_bp = Blueprint("prog_bp", __name__)

prog_root = "/prog"

PROG_ENDPOINTS = [
    "infix-to-prefix",
    "infix-to-postfix",
    "prefix-to-infix",
    "postfix-to-infix",
    "prefix-to-postfix",
    "postfix-to-prefix",
    "eval-prefix",
    "eval-postfix",
    "sort-bubble",
    "sort-insertion",
    "sort-selection",
    "sort-merge",
    "sort-quick",
]
PROG_DETAILED_ENDPOINTS = ["<endpoint>/theory"]

from .algos import Sort

s = Sort  #


@prog_bp.route(prog_root)
def prog_home():
    return {
        "api-name": "prog",
        "purpose": "algos and conversions",
        "endpoints": PROG_ENDPOINTS,
        "endpoints-detailed": PROG_DETAILED_ENDPOINTS,
    }


# theory


@prog_bp.route(prog_root + "/<string:algo>/theory")
def prog_theory(algo):
    t = ProgTheory.find_algo_by_route(algo)
    if t:
        return t.json()
    else:
        return {"error": "algo not found"}
