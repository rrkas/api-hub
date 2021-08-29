from app.prog.algos import AdvancedAlgorithms, Documentation, ReqponseBodyItem
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
    except BaseException as e:
        response["error"] = str(e)
        return response
    try:
        vals = list(map(float, vals.split()))
    except BaseException as e:
        response["error"] = str(e)
        return response
    try:
        capacity = float(capacity)
    except BaseException as e:
        response["error"] = str(e)
        return response
    response["capacity"] = capacity
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
    except BaseException as e:
        response["error"] = str(e)
        return response
    try:
        ends = list(map(int, ends.split()))
    except BaseException as e:
        response["error"] = str(e)
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
    except BaseException as e:
        response["error"] = str(e)
        return response
    try:
        ends = list(map(int, ends.split()))
    except BaseException as e:
        response["error"] = str(e)
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
    except BaseException as e:
        return {"n": n, "error": str(e)}
    return AdvancedAlgorithms.n_queens(n)


def advanced_docs():
    subject = "Programming"
    category = "Greedy Algorithms"
    data = [
        Documentation(
            subject=subject,
            category=category,
            name='Fractional Knapsack',
            method="POST",
            endpoint=prog_root + "/knapsack-fractional",
            description='Given weights and values of n items, we need to put these items in a knapsack of capacity W \
to get the maximum total value in the knapsack. Note: an item can be taken fully, partially or ignored.',
            theory='The basic idea is to calculate the ratio value/weight for each item and sort the item on basis of \
this ratio. Then take the item with the highest ratio and add them until we can’t add the next item as a whole and at \
the end add the next item as much as we can. Which will always be the optimal solution to this problem.',
            inp_body=[
                ReqponseBodyItem(
                    key="weighs",
                    desc='space separated weighs of items',
                    types=[ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    key="vals",
                    desc='space separated values of items',
                    types=[ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    key="capacity",
                    desc='capacity of the knapsack (bag)',
                    types=[ReqponseBodyItem.TYPE_FLOAT],
                ),
            ],
            out_body=[
                ReqponseBodyItem(
                    key="weighs",
                    desc='space separated weighs of items',
                    types=[ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    key="vals",
                    desc='space separated values of items',
                    types=[ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    key="capacity",
                    desc='capacity of the knapsack (bag)',
                    types=[ReqponseBodyItem.TYPE_FLOAT],
                ),
                ReqponseBodyItem(
                    key="result",
                    desc="max value",
                    types=[ReqponseBodyItem.TYPE_FLOAT]
                ),
                ReqponseBodyItem(
                    key="error",
                    desc="error message",
                    types=[ReqponseBodyItem.TYPE_STR]
                ),
            ],
            sample_inp_body={
                "weighs": "10 40 20 30",
                "vals": "60 40 100 120",
                "capacity": 50,
            },
            sample_out_body={
                "capacity": 50.0,
                "result": 240.0,
                "vals": "60 40 100 120",
                "weighs": "10 40 20 30"
            },
            py_code="""
def frac_knap(weighs, vals, capacity):
    if sum(weighs) <= capacity:
        return sum(vals)
    class Item:
        def __init__(self, w, v, idx):
            self.w = w
            self.v = v
            self.idx = idx
            self.cost = v / w

        def __lt__(self, other):
            return self.cost < other.cost

    items = []
    for i in range(len(vals)):
        items.append(Item(weighs[i], vals[i], i))

    items.sort(reverse=True)

    total_value = 0
    for i in items:
        cur_wt = i.w
        cur_val = i.v
        if capacity - cur_wt >= 0:
            capacity -= cur_wt
            total_value += cur_val
        else:
            fraction = capacity / cur_wt
            total_value += cur_val * fraction
            break

    return total_value
            """,

        ),

    ]
    category = 'Dynamic Programming'
    data += []
    return data
