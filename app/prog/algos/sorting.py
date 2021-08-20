from flask import request

from app.prog.routes import prog_bp, prog_root
from . import Sort
from ...util import type_error_message, get_value_form_json


@prog_bp.route(prog_root + "/sort-bubble", methods=["POST"])
def prog_sort_bubble():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    inp = get_value_form_json(expr_key)
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    try:
        inp = list(map(int, inp.split()))
    except BaseException:
        try:
            inp = list(map(float, inp.split()))
        except BaseException:
            return {"arr": inp, "error": type_error_message([1, 1.0], inp.split()[0])}
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
    inp = get_value_form_json(expr_key)
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    try:
        inp = list(map(int, inp.split()))
    except BaseException:
        try:
            inp = list(map(float, inp.split()))
        except BaseException:
            return {"arr": inp, "error": type_error_message([1, 1.0], inp.split()[0])}
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
    inp = get_value_form_json(expr_key)
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    try:
        inp = list(map(int, inp.split()))
    except BaseException:
        try:
            inp = list(map(float, inp.split()))
        except BaseException:
            return {"arr": inp, "error": type_error_message([1, 1.0], inp.split()[0])}
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
    inp = get_value_form_json(expr_key)
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    try:
        inp = list(map(int, inp.split()))
    except BaseException:
        try:
            inp = list(map(float, inp.split()))
        except BaseException:
            return {"arr": inp, "error": type_error_message([1, 1.0], inp.split()[0])}
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
    inp = get_value_form_json(expr_key)
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    try:
        inp = list(map(int, inp.split()))
    except BaseException:
        try:
            inp = list(map(float, inp.split()))
        except BaseException:
            return {"arr": inp, "error": type_error_message([1, 1.0], inp.split()[0])}
    res = Sort.quick_sort(inp)
    return res.json()


@prog_bp.route(prog_root + "/sort-counting", methods=["POST"])
def prog_sort_counting():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    inp = get_value_form_json(expr_key)
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    try:
        inp = list(map(int, inp.split()))
    except BaseException:
        return {"arr": inp, "error": type_error_message([1], inp.split()[0])}
    res = Sort.counting_sort(inp)
    return res.json()


@prog_bp.route(prog_root + "/sort-radix", methods=["POST"])
def prog_sort_radix():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    inp = get_value_form_json(expr_key)
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    try:
        inp = list(map(int, inp.split()))
    except BaseException:
        return {"arr": inp, "error": type_error_message([1], inp.split()[0])}
    res = Sort.radix_sort(inp)
    return res.json()


@prog_bp.route(prog_root + "/sort-bucket", methods=["POST"])
def prog_sort_bucket():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    inp = get_value_form_json(expr_key)
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    try:
        inp = list(map(float, inp.split()))
    except BaseException:
        return {"arr": inp, "error": type_error_message([1, 1.0], inp.split()[0])}
    res = Sort.bucket_sort(inp)
    return res.json()


@prog_bp.route(prog_root + "/sort-heap", methods=["POST"])
def prog_sort_heap():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    inp = get_value_form_json(expr_key)
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    try:
        inp = list(map(int, inp.split()))
    except BaseException:
        try:
            inp = list(map(float, inp.split()))
        except BaseException:
            return {"arr": inp, "error": type_error_message([1, 1.0], inp.split()[0])}
    res = Sort.heap_sort(inp)
    return res.json()


@prog_bp.route(prog_root + "/sort-shell", methods=["POST"])
def prog_sort_shell():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    inp = get_value_form_json(expr_key)
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    try:
        inp = list(map(int, inp.split()))
    except BaseException:
        try:
            inp = list(map(float, inp.split()))
        except BaseException:
            return {"arr": inp, "error": type_error_message([1, 1.0], inp.split()[0])}
    res = Sort.shell_sort(inp)
    return res.json()
