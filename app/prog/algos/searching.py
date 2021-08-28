from flask import request

from app.prog.routes import prog_bp, prog_root
from . import Search
from ...models import Documentation, ReqponseBodyItem, ComplexityAnalysis
from ...util import get_value_form_json


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
        inp = list(map(int, inp.split()))
    except BaseException as e1:
        try:
            inp = list(map(float, inp.split()))
        except BaseException as e2:
            return {"arr": inp, "error": str(e1) + "; " + str(e2)}
    x = get_value_form_json(expr_keys[1])
    try:
        x = int(x)
        if not isinstance(inp[0], int):
            return {
                "error": f"type of array elements dont match type of {expr_keys[1]}"
            }
    except BaseException as e1:
        try:
            x = float(x)
            if not isinstance(inp[0], float):
                return {
                    "error": f"type of array elements dont match type of {expr_keys[1]}"
                }
        except BaseException as e2:
            return {"error": str(e1) + "; " + str(e2)}
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
            time_complexity=ComplexityAnalysis(best=1, worst="n", average="n/2"),
            space_complexity=ComplexityAnalysis(1, 1, 1),
            py_code="""
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
index = linear_search(arr, x)
            """,
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Binary Search",
            description="Searches element in a list of elements",
            endpoint=prog_root + "/search-binary",
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
                    [ReqponseBodyItem.TYPE_FLOAT, ReqponseBodyItem.TYPE_INT],
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
                ),
            ],
            sample_inp_body={
                "arr": "1 2 3 4",
                "key": 2,
            },
            sample_out_body={
                "algorithm": "Binary Search",
                "arr": "1 2 3 4",
                "comparisons": 2,
                "found": True,
                "index": 1,
                "key": 2,
                "time_taken": "0 milliseconds",
            },
            time_complexity=ComplexityAnalysis(best=1, worst="log n", average="log n"),
            space_complexity=ComplexityAnalysis(1, 1, 1),
            py_code="""
def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1
index = binary_search(arr, 0, len(arr) - 1, x)
            """,
        ),
    ]
