from flask import request

from app.prog.routes import prog_bp, prog_root
from . import Sort, Documentation, ReqponseBodyItem
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
            return {"arr": inp, "error": type_error_message([1, 1.0], inp)}
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
            return {"arr": inp, "error": type_error_message([1, 1.0], inp)}
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
            return {"arr": inp, "error": type_error_message([1, 1.0], inp)}
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
            return {"arr": inp, "error": type_error_message([1, 1.0], inp)}
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
            return {"arr": inp, "error": type_error_message([1, 1.0], inp)}
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
        return {"arr": inp, "error": type_error_message([1], inp)}
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
        return {"arr": inp, "error": type_error_message([1], inp)}
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
        if any([i >= 1 for i in inp]):
            raise TypeError("")
    except BaseException:
        return {"arr": " ".join(map(str, inp)), "error": type_error_message([1.0], inp)}
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
            return {"arr": inp, "error": type_error_message([1, 1.0], inp)}
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
            return {"arr": inp, "error": type_error_message([1, 1.0], inp)}
    res = Sort.shell_sort(inp)
    return res.json()


def sorting_docs():
    data = []
    category = "Sorting"
    data.append(
        Documentation(
            category=category,
            name="Bubble Sort",
            description="Sorts array of integers, float/double using bubble sort algorithm.",
            endpoint=prog_root + "/sort-bubble",
            sample_request_url=prog_root + "/sort-bubble",
            args=None,
            method="POST",
            inp_body=[
                ReqponseBodyItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseBodyItem.TYPE_STR],
                )
            ],
            out_body=[
                ReqponseBodyItem(
                    "algorithm", "name of algorithm used", [ReqponseBodyItem.TYPE_STR]
                ),
                ReqponseBodyItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    "result",
                    "space separated numbers (output)",
                    [ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    "time_taken",
                    "time taken (milliseconds) to complete the algorithm",
                    [ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    "error",
                    "error message",
                    [ReqponseBodyItem.TYPE_STR],
                    optional=True,
                ),
            ],
            sample_inp_body={
                "arr": "15 12 1 0 -8 9 4",
            },
            sample_out_body={
                "algorithm": "Bubble Sort",
                "arr": "15 12 1 0 -8 9 4",
                "result": "-8 0 1 4 9 12 15",
                "time_taken": "0 milliseconds",
            },
            theory=""
        )
    )
    data.append(
        Documentation(
            category=category,
            name="Insertion Sort",
            description="Sorts array of integers, float/double using insertion sort algorithm.",
            endpoint=prog_root + "/sort-insertion",
            sample_request_url=prog_root + "/sort-insertion",
            args=None,
            method="POST",
            inp_body=[
                ReqponseBodyItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseBodyItem.TYPE_STR],
                )
            ],
            out_body=[
                ReqponseBodyItem(
                    "algorithm",
                    "name of algorithm used",
                    [ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    "result",
                    "space separated numbers (output)",
                    [ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    "time_taken",
                    "time taken (milliseconds) to complete the algorithm",
                    [ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    "error",
                    "error message",
                    [ReqponseBodyItem.TYPE_STR],
                    optional=True,
                ),
            ],
            sample_inp_body={
                "arr": "15 12 1 0 -8 9 4",
            },
            sample_out_body={
                "algorithm": "Insertion Sort",
                "arr": "15 12 1 0 -8 9 4",
                "result": "-8 0 1 4 9 12 15",
                "time_taken": "0 milliseconds",
            },
        )
    )
    return data
