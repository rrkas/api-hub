from flask import request

from app.prog.routes import prog_bp, prog_root
from . import Search
from ...util import type_error_message


@prog_bp.route(prog_root + "/search-linear", methods=["POST"])
def prog_search_linear():
    expr_keys = ["arr", "key"]
    for key in expr_keys:
        if key not in request.form.keys() and key not in (request.json or {}).keys():
            return {"error": f"{key} missing in body!"}
    if expr_keys[0] in request.form.keys():
        inp = request.form.get(expr_keys[0])
    else:
        inp = request.json[expr_keys[0]]
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    inp = inp.split()
    if expr_keys[1] in request.form.keys():
        x = request.form.get(expr_keys[1])
    else:
        x = request.json[expr_keys[1]]
    res = Search.linear_search(inp, x)
    return res.json()


@prog_bp.route(prog_root + "/search-binary", methods=["POST"])
def prog_search_binary():
    expr_keys = ["arr", "key"]
    for key in expr_keys:
        if key not in request.form.keys() and key not in (request.json or {}).keys():
            return {"error": f"{key} missing in body!"}
    if expr_keys[0] in request.form.keys():
        inp = request.form.get(expr_keys[0])
    else:
        inp = request.json[expr_keys[0]]
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    try:
        inp = list(map(int, inp.split()))
    except:
        try:
            inp = list(map(float, inp.split()))
        except:
            return {
                "error": type_error_message([1, 1.0], inp.split()[0], arg=expr_keys[0])
            }
    if expr_keys[1] in request.form.keys():
        x = request.form.get(expr_keys[1])
    else:
        x = request.json[expr_keys[1]]
    try:
        x = int(x)
        if not isinstance(inp[0], int):
            return {"error": type_error_message([inp[0]], x, arg=expr_keys[1])}
    except:
        try:
            x = float(x)
            if not isinstance(inp[0], float):
                return {"error": type_error_message([inp[0]], x, arg=expr_keys[1])}
        except:
            return {"error": type_error_message([1, 1.0], x, arg=expr_keys[1])}
    res = Search.binary_search(inp, x)
    return res.json()
