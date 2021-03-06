from flask import request

from app.prog.routes import prog_bp, prog_root
from . import Search
from ...models import Documentation, ReqponseItem, ComplexityAnalysis
from ...util import get_value_form_json


@prog_bp.route(prog_root + "/search-linear", methods=["POST"])
def prog_search_linear():
    expr_keys = ["arr", "key"]
    for key in expr_keys:
        if key not in request.form.keys() and key not in (request.json or {}).keys():
            return {"error": f"{key} missing in body!"}
    inp = get_value_form_json(expr_keys[0])
    x = get_value_form_json(expr_keys[1])
    data = {
        "arr": inp,
        "key": x,
    }
    if " " not in inp:
        data.update({"error": "please separate numbers using spaces!"})
        return data
    inp = inp.split()
    res = Search.linear_search(inp, x)
    return res.json()


@prog_bp.route(prog_root + "/search-binary", methods=["POST"])
def prog_search_binary():
    expr_keys = ["arr", "key"]
    for key in expr_keys:
        if key not in request.form.keys() and key not in (request.json or {}).keys():
            return {"error": f"{key} missing in body!"}
    arr = get_value_form_json(expr_keys[0])
    x = get_value_form_json(expr_keys[1])
    data = {
        "arr": arr,
        "key": x,
    }
    if " " not in arr:
        data.update({"error": "please separate numbers using spaces!"})
        return data
    try:
        arr = list(map(int, arr.split()))
        t = arr[:]
        t.sort()
        if t != arr:
            data.update({"error": "Input array is not in non-decreasing order!"})
            return data
    except BaseException as e1:
        try:
            arr = list(map(float, arr.split()))
        except BaseException as e2:
            data.update({"error": str(e1) + "; " + str(e2)})
            return data
    try:
        x = int(x)
        if not isinstance(arr[0], int):
            data.update(
                {"error": f"type of array elements dont match type of {expr_keys[1]}"}
            )
            return data
    except BaseException as e1:
        try:
            x = float(x)
            if not isinstance(arr[0], float):
                data.update(
                    {
                        "error": f"type of array elements dont match type of {expr_keys[1]}"
                    }
                )
                return data
        except BaseException as e2:
            data.update({"error": str(e1) + "; " + str(e2)})
            return data
    res = Search.binary_search(arr, x)
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
                ReqponseItem(
                    key="arr",
                    desc="space-separated elements",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "key",
                    "element to find",
                    [
                        ReqponseItem.TYPE_FLOAT,
                        ReqponseItem.TYPE_INT,
                        ReqponseItem.TYPE_STR,
                    ],
                ),
            ],
            out_body=[
                ReqponseItem(
                    "algorithm",
                    "Name of algorithm",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "arr",
                    "space-separated elements (input)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "key",
                    "element to find (input)",
                    [
                        ReqponseItem.TYPE_FLOAT,
                        ReqponseItem.TYPE_INT,
                        ReqponseItem.TYPE_STR,
                    ],
                ),
                ReqponseItem(
                    "found",
                    "is element found",
                    [ReqponseItem.TYPE_BOOL],
                ),
                ReqponseItem(
                    "time_taken",
                    "time taken (milliseconds) to complete the algorithm",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "comparisons",
                    "number of comparisons made",
                    [ReqponseItem.TYPE_INT],
                ),
                ReqponseItem(
                    "index",
                    "index of element in list",
                    [ReqponseItem.TYPE_INT],
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
                ReqponseItem(
                    key="arr",
                    desc="space-separated elements",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "key",
                    "element to find",
                    [
                        ReqponseItem.TYPE_FLOAT,
                        ReqponseItem.TYPE_INT,
                        ReqponseItem.TYPE_STR,
                    ],
                ),
            ],
            out_body=[
                ReqponseItem(
                    "algorithm",
                    "Name of algorithm",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "arr",
                    "space-separated elements (input)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "key",
                    "element to find (input)",
                    [ReqponseItem.TYPE_FLOAT, ReqponseItem.TYPE_INT],
                ),
                ReqponseItem(
                    "found",
                    "is element found",
                    [ReqponseItem.TYPE_BOOL],
                ),
                ReqponseItem(
                    "time_taken",
                    "time taken (milliseconds) to complete the algorithm",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "comparisons",
                    "number of comparisons made",
                    [ReqponseItem.TYPE_INT],
                ),
                ReqponseItem(
                    "index",
                    "index of element in list",
                    [ReqponseItem.TYPE_INT],
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
