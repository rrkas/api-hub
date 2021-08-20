from flask import Blueprint

from app.prog.theory import ProgTheory

prog_bp = Blueprint("prog_bp", __name__)

prog_root = "/prog"

PROG_DETAILED_ENDPOINTS = ["<endpoint>/theory"]

from .algos import Sort

s = Sort  # just so that import doesn't get removed during optimized


@prog_bp.route(prog_root + "/<string:algo>/theory")
def prog_theory(algo):
    t = ProgTheory.find_algo_by_route(algo)
    if t:
        return t.json()
    else:
        return {"error": "algo not found"}
