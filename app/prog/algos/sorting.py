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
    arr = get_value_form_json(expr_key)
    if " " not in arr:
        return {"error": "please separate numbers using spaces!"}
    try:
        arr = list(map(int, arr.split()))
    except BaseException:
        try:
            arr = list(map(float, arr.split()))
        except BaseException:
            return {"arr": arr, "error": type_error_message([1, 1.0], arr)}
    res = Sort.bubble_sort(arr)
    return res.json()


@prog_bp.route(prog_root + "/sort-insertion", methods=["POST"])
def prog_sort_insertion():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    if " " not in arr:
        return {"error": "please separate numbers using spaces!"}
    try:
        arr = list(map(int, arr.split()))
    except BaseException:
        try:
            arr = list(map(float, arr.split()))
        except BaseException:
            return {"arr": arr, "error": type_error_message([1, 1.0], arr)}
    res = Sort.insertion_sort(arr)
    return res.json()


@prog_bp.route(prog_root + "/sort-selection", methods=["POST"])
def prog_sort_selection():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    if " " not in arr:
        return {"error": "please separate numbers using spaces!"}
    try:
        arr = list(map(int, arr.split()))
    except BaseException:
        try:
            arr = list(map(float, arr.split()))
        except BaseException:
            return {"arr": arr, "error": type_error_message([1, 1.0], arr)}
    res = Sort.selection_sort(arr)
    return res.json()


@prog_bp.route(prog_root + "/sort-merge", methods=["POST"])
def prog_sort_merge():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    if " " not in arr:
        return {"error": "please separate numbers using spaces!"}
    try:
        arr = list(map(int, arr.split()))
    except BaseException:
        try:
            arr = list(map(float, arr.split()))
        except BaseException:
            return {"arr": arr, "error": type_error_message([1, 1.0], arr)}
    res = Sort.merge_sort(arr)
    return res.json()


@prog_bp.route(prog_root + "/sort-quick", methods=["POST"])
def prog_sort_quick():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    if " " not in arr:
        return {"error": "please separate numbers using spaces!"}
    try:
        arr = list(map(int, arr.split()))
    except BaseException:
        try:
            arr = list(map(float, arr.split()))
        except BaseException:
            return {"arr": arr, "error": type_error_message([1, 1.0], arr)}
    res = Sort.quick_sort(arr)
    return res.json()


@prog_bp.route(prog_root + "/sort-counting", methods=["POST"])
def prog_sort_counting():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    if " " not in arr:
        return {"error": "please separate numbers using spaces!"}
    try:
        arr = list(map(int, arr.split()))
    except BaseException:
        return {"arr": arr, "error": type_error_message([1], arr)}
    res = Sort.counting_sort(arr)
    return res.json()


@prog_bp.route(prog_root + "/sort-radix", methods=["POST"])
def prog_sort_radix():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    if " " not in arr:
        return {"error": "please separate numbers using spaces!"}
    try:
        arr = list(map(int, arr.split()))
    except BaseException:
        return {"arr": arr, "error": type_error_message([1], arr)}
    res = Sort.radix_sort(arr)
    return res.json()


@prog_bp.route(prog_root + "/sort-bucket", methods=["POST"])
def prog_sort_bucket():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    if " " not in arr:
        return {"error": "please separate numbers using spaces!"}
    try:
        arr = list(map(float, arr.split()))
        if any([i >= 1 for i in arr]):
            raise TypeError("")
    except BaseException:
        return {"arr": " ".join(map(str, arr)), "error": type_error_message([1.0], arr)}
    res = Sort.bucket_sort(arr)
    return res.json()


@prog_bp.route(prog_root + "/sort-heap", methods=["POST"])
def prog_sort_heap():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    if " " not in arr:
        return {"error": "please separate numbers using spaces!"}
    try:
        arr = list(map(int, arr.split()))
    except BaseException:
        try:
            arr = list(map(float, arr.split()))
        except BaseException:
            return {"arr": arr, "error": type_error_message([1, 1.0], arr)}
    res = Sort.heap_sort(arr)
    return res.json()


@prog_bp.route(prog_root + "/sort-shell", methods=["POST"])
def prog_sort_shell():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    if " " not in arr:
        return {"error": "please separate numbers using spaces!"}
    try:
        arr = list(map(int, arr.split()))
    except BaseException:
        try:
            arr = list(map(float, arr.split()))
        except BaseException:
            return {"arr": arr, "error": type_error_message([1, 1.0], arr)}
    res = Sort.shell_sort(arr)
    return res.json()


def sorting_docs():
    data = []
    subject = "Programming"
    category = "Sorting"
    data.append(
        Documentation(
            subject=subject,
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
            theory="This sorting algorithm is comparison-based algorithm in which each pair of adjacent elements \
is compared and the elements are swapped if they are not in order.",
            py_code="""
n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    """
        )
    )
    data.append(
        Documentation(
            subject=subject,
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
            theory="The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are \
picked and placed at the correct position in the sorted part.",
            py_code="""
for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
            """,
        )
    )
    data.append(
        Documentation(
            subject=subject,
            category=category,
            name="Selection Sort",
            description="Sorts array of integers, float/double using selection sort algorithm.",
            endpoint=prog_root + "/sort-selection",
            sample_request_url=prog_root + "/sort-selection",
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
                "algorithm": "Selection Sort",
                "arr": "15 12 1 0 -8 9 4",
                "result": "-8 0 1 4 9 12 15",
                "time_taken": "0 milliseconds",
            },
            theory="The smallest element is selected from the unsorted array and swapped with the leftmost element, \
and that element becomes a part of the sorted array. This process continues moving unsorted array boundary by \
one element to the right.",
            py_code="""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
                """,
        )
    )
    return data
