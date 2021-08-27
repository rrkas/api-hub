from app.prog.algos import AdvancedAlgorithms
from app.prog.routes import prog_bp, prog_root
from app.util import *


# greedy algos
@prog_bp.route(prog_root + "/knapsack-fractional", methods=["POST"])
def prog_knapsack_fractional():
    expr_keys = ["weighs", "vals", "capacity"]
    for expr_key in expr_keys:
        if (
            expr_key not in request.form.keys()
            and expr_key not in (request.json or {}).keys()
        ):
            return {"error": f"{expr_key} missing in body!"}
    weighs = get_value_form_json(expr_keys[0])
    vals = get_value_form_json(expr_keys[1])
    capacity = get_value_form_json(expr_keys[2])
    response = {
        "weighs": weighs,
        "vals": vals,
        "capacity": capacity,
    }
    try:
        weighs = list(map(float, weighs.split()))
    except:
        response["error"] = type_error_message([1, 1.0], weighs)
        return response
    try:
        vals = list(map(float, vals.split()))
    except:
        response["error"] = type_error_message([1, 1.0], vals)
        return response
    try:
        capacity = float(capacity)
    except:
        response["error"] = type_error_message([1, 1.0], capacity)
        return response
    res, err = AdvancedAlgorithms.knapsack_fractional(weighs, vals, capacity)
    if err:
        response["error"] = res
    else:
        response["result"] = res
    return response


@prog_bp.route(prog_root + "/activity-selection", methods=["POST"])
def prog_activity_selection():
    expr_keys = ["starts", "ends"]
    for expr_key in expr_keys:
        if (
            expr_key not in request.form.keys()
            and expr_key not in (request.json or {}).keys()
        ):
            return {"error": f"{expr_key} missing in body!"}
    starts = get_value_form_json(expr_keys[0])
    ends = get_value_form_json(expr_keys[1])
    response = {
        "starts": starts,
        "ends": ends,
    }
    try:
        starts = list(map(int, starts.split()))
    except:
        response["error"] = type_error_message([1], starts)
        return response
    try:
        ends = list(map(int, ends.split()))
    except:
        response["error"] = type_error_message([1], ends)
        return response

    res, err = AdvancedAlgorithms.activity_selection(starts, ends)
    if err:
        response["error"] = res
    else:
        response["result"] = str(res)
    return response


@prog_bp.route(prog_root + "/job-sequencing", methods=["POST"])
def prog_job_sequencing():
    expr_keys = ["ids", "deadlines", "profits"]
    for expr_key in expr_keys:
        if (
            expr_key not in request.form.keys()
            and expr_key not in (request.json or {}).keys()
        ):
            return {"error": f"{expr_key} missing in body!"}
    starts = get_value_form_json(expr_keys[0])
    ends = get_value_form_json(expr_keys[1])
    response = {
        "starts": starts,
        "ends": ends,
    }
    try:
        starts = list(map(int, starts.split()))
    except:
        response["error"] = type_error_message([1], starts)
        return response
    try:
        ends = list(map(int, ends.split()))
    except:
        response["error"] = type_error_message([1], ends)
        return response

    res, err = AdvancedAlgorithms.activity_selection(starts, ends)
    if err:
        response["error"] = res
    else:
        response["result"] = str(res)
    return response


@prog_bp.route(prog_root + "/huffman-code", methods=["POST"])
def prog_huffman_code():
    expr_keys = ["inp"]
    for expr_key in expr_keys:
        if (
            expr_key not in request.form.keys()
            and expr_key not in (request.json or {}).keys()
        ):
            return {"error": f"{expr_key} missing in body!"}
    inp = get_value_form_json(expr_keys[0])
    return AdvancedAlgorithms.huffman_code(inp)


# dynamic programming


@prog_bp.route(prog_root + "/longest-common-subsequence", methods=["POST"])
def prog_lcs():
    expr_keys = ["str1", "str2"]
    for expr_key in expr_keys:
        if (
            expr_key not in request.form.keys()
            and expr_key not in (request.json or {}).keys()
        ):
            return {"error": f"{expr_key} missing in body!"}
    str1 = get_value_form_json(expr_keys[0])
    str2 = get_value_form_json(expr_keys[1])
    lcs = AdvancedAlgorithms.longest_common_subsequence(str1, str2)
    return {
        "str1": str1,
        "str2": str2,
        "lcs": lcs,
    }


@prog_bp.route(prog_root + "/n-queens", methods=["POST"])
def prog_n_queens():
    expr_keys = ["n"]
    for expr_key in expr_keys:
        if (
            expr_key not in request.form.keys()
            and expr_key not in (request.json or {}).keys()
        ):
            return {"error": f"{expr_key} missing in body!"}
    n = get_value_form_json(expr_keys[0])
    try:
        n = int(n)
    except:
        return {"n": n, "error": type_error_message([1], n)}
    return AdvancedAlgorithms.n_queens(n)


def advanced_docs():
    subject = "Programming"
    category = "Advanced Algorithms"
    return []
