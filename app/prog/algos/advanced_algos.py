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
        weighs = list(map(int, weighs.split()))
    except:
        try:
            weighs = list(map(float, weighs.split()))
        except:
            response["error"] = type_error_message([1, 1.0], weighs)
            return response
    try:
        vals = list(map(int, vals.split()))
    except:
        try:
            vals = list(map(float, vals.split()))
        except:
            response["error"] = type_error_message([1, 1.0], vals)
            return response
    try:
        capacity = int(capacity)
    except:
        try:
            capacity = float(capacity)
        except:
            response["error"] = type_error_message([1, 1.0], capacity)
            return response
    res, err = AdvancedAlgorithms.fractional_knapsack(weighs, vals, capacity)
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
