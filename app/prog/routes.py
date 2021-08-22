from flask import Blueprint

prog_bp = Blueprint("prog_bp", __name__)

prog_root = "/prog"

PROG_DETAILED_ENDPOINTS = ["<endpoint>/theory"]

from .algos import Sort

s = Sort  # just so that import doesn't get removed during optimized
