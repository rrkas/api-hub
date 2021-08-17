from flask import request

from app.prog.routes import prog_bp, prog_root
from . import Sort


@prog_bp.route(prog_root + "/sort-bubble", methods=["POST"])
def prog_sort_bubble():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    if expr_key in request.form.keys():
        inp = request.form.get(expr_key)
    else:
        inp = request.json[expr_key]
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    inp = list(map(int, inp.split()))
    res = Sort.bubble_sort(inp)
    return res.json()


@prog_bp.route(prog_root + "/sort-insertion", methods=["POST"])
def prog_sort_insertion():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    if expr_key in request.form.keys():
        inp = request.form.get(expr_key)
    else:
        inp = request.json[expr_key]
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    inp = list(map(int, inp.split()))
    res = Sort.insertion_sort(inp)
    return res.json()


@prog_bp.route(prog_root + "/sort-selection", methods=["POST"])
def prog_sort_selection():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    if expr_key in request.form.keys():
        inp = request.form.get(expr_key)
    else:
        inp = request.json[expr_key]
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    inp = list(map(int, inp.split()))
    res = Sort.selection_sort(inp)
    return res.json()


@prog_bp.route(prog_root + "/sort-merge", methods=["POST"])
def prog_sort_merge():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    if expr_key in request.form.keys():
        inp = request.form.get(expr_key)
    else:
        inp = request.json[expr_key]
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    inp = list(map(int, inp.split()))
    res = Sort.merge_sort(inp)
    return res.json()


@prog_bp.route(prog_root + "/sort-quick", methods=["POST"])
def prog_sort_quick():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    if expr_key in request.form.keys():
        inp = request.form.get(expr_key)
    else:
        inp = request.json[expr_key]
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    inp = list(map(int, inp.split()))
    res = Sort.quick_sort(inp)
    return res.json()
