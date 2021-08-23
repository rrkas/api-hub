from flask import request

from app.prog.routes import prog_bp, prog_root
from . import Search
from ...models import Documentation, ReqponseBodyItem
from ...util import type_error_message, get_value_form_json


@prog_bp.route(prog_root + "/search-linear", methods=["POST"])
def prog_search_linear():
    expr_keys = ["arr", "key"]
    for key in expr_keys:
        if key not in request.form.keys() and key not in (request.json or {}).keys():
            return {"error": f"{key} missing in body!"}
    inp = get_value_form_json(expr_keys[0])
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    inp = inp.split()
    x = get_value_form_json(expr_keys[1])
    res = Search.linear_search(inp, x)
    return res.json()


@prog_bp.route(prog_root + "/search-binary", methods=["POST"])
def prog_search_binary():
    expr_keys = ["arr", "key"]
    for key in expr_keys:
        if key not in request.form.keys() and key not in (request.json or {}).keys():
            return {"error": f"{key} missing in body!"}
    inp = get_value_form_json(expr_keys[0])
    if " " not in inp:
        return {"error": "please separate numbers using spaces!"}
    try:
        inp = list(map(float, inp.split()))
    except:
        return {"error": type_error_message([1, 1.0], inp.split()[0], arg=expr_keys[0])}
    x = get_value_form_json(expr_keys[1])
    try:
        x = float(x)
        if not isinstance(inp[0], float):
            return {"error": type_error_message([inp[0]], x, arg=expr_keys[1])}
    except:
        return {"error": type_error_message([1, 1.0], x, arg=expr_keys[1])}
    res = Search.binary_search(inp, x)
    return res.json()


def searching_docs():
    subject = "Programming"
    category = "Searching"
    return [
        Documentation(
            subject=subject,
            category=category,
            name="Linear Search",
            description="Searches element in a list of elements",
            endpoint=prog_root + "/search-linear",
            sample_request_url=prog_root + "/search-linear",
            method="POST",
            inp_body=[
                ReqponseBodyItem(
                    key="arr",
                    desc="space-separated elements",
                    types=[ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    "key",
                    "element to find",
                    [
                        ReqponseBodyItem.TYPE_FLOAT,
                        ReqponseBodyItem.TYPE_INT,
                        ReqponseBodyItem.TYPE_STR,
                    ],
                ),
            ],
            out_body=[
                ReqponseBodyItem(
                    "algorithm",
                    "Name of algorithm",
                    [ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    "arr",
                    "space-separated elements (input)",
                    [ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    "key",
                    "element to find (input)",
                    [
                        ReqponseBodyItem.TYPE_FLOAT,
                        ReqponseBodyItem.TYPE_INT,
                        ReqponseBodyItem.TYPE_STR,
                    ],
                ),
                ReqponseBodyItem(
                    "found",
                    "is element found",
                    [ReqponseBodyItem.TYPE_BOOL],
                ),
                ReqponseBodyItem(
                    "time_taken",
                    "time taken (milliseconds) to complete the algorithm",
                    [ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    "comparisons",
                    "number of comparisons made",
                    [ReqponseBodyItem.TYPE_INT],
                ),
                ReqponseBodyItem(
                    "index",
                    "index of element in list",
                    [ReqponseBodyItem.TYPE_INT],
                    optional=True,
                ),
            ],
            sample_inp_body={
                "arr": "1z 2b 3d 4a",
                "key": "2b",
            },
            sample_out_body={
                "algorithm": "Linear Search",
                "arr": "1z 2b 3d 4a",
                "comparisons": 2,
                "found": True,
                "index": 1,
                "key": "2b",
                "time_taken": "0 milliseconds",
            },
        )
    ]
