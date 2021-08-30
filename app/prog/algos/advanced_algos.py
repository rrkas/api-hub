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
    data = {"n": n}
    try:
        n = int(n)
    except BaseException as e:
        data.update({"error": str(e)})
        return data
    return AdvancedAlgorithms.n_queens(n)


def advanced_docs():
    subject = "Programming"
    category = "Greedy Algorithms"
    data = [
        Documentation(
            subject=subject,
            category=category,
            name="Fractional Knapsack",
            method="POST",
            endpoint=prog_root + "/knapsack-fractional",
            description="Given weights and values of n items, we need to put these items in a knapsack of capacity W \
to get the maximum total value in the knapsack. Note: an item can be taken fully, partially or ignored.",
            theory="The basic idea is to calculate the ratio value/weight for each item and sort the item on basis of \
this ratio. Then take the item with the highest ratio and add them until we can’t add the next item as a whole and at \
the end add the next item as much as we can. Which will always be the optimal solution to this problem.",
            inp_body=[
                ReqponseBodyItem(
                    key="weighs",
                    desc="space separated weighs of items",
                    types=[ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    key="vals",
                    desc="space separated values of items",
                    types=[ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    key="capacity",
                    desc="capacity of the knapsack (bag)",
                    types=[ReqponseBodyItem.TYPE_FLOAT],
                ),
            ],
            out_body=[
                ReqponseBodyItem(
                    key="weighs",
                    desc="space separated weighs of items",
                    types=[ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    key="vals",
                    desc="space separated values of items",
                    types=[ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    key="capacity",
                    desc="capacity of the knapsack (bag)",
                    types=[ReqponseBodyItem.TYPE_FLOAT],
                ),
                ReqponseBodyItem(
                    key="result", desc="max value", types=[ReqponseBodyItem.TYPE_FLOAT]
                ),
                ReqponseBodyItem(
                    key="error", desc="error message", types=[ReqponseBodyItem.TYPE_STR]
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
                "weighs": "10 40 20 30",
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
        Documentation(
            subject=subject,
            category=category,
            name="Activity Selection",
            method="POST",
            endpoint=prog_root + "/activity-selection",
            description="",
            theory="",
            inp_body=[
                ReqponseBodyItem(
                    key="starts",
                    desc="space separated start time of activities",
                    types=[ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    key="ends",
                    desc="space separated end time of activities",
                    types=[ReqponseBodyItem.TYPE_STR],
                ),
            ],
            out_body=[
                ReqponseBodyItem(
                    key="starts",
                    desc="space separated start time of activities",
                    types=[ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    key="ends",
                    desc="space separated end time of activities",
                    types=[ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    key="result",
                    desc="jsonified list of list of start and end times of optimized activities",
                    types=[ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    key="error", desc="error message", types=[ReqponseBodyItem.TYPE_STR]
                ),
            ],
            sample_inp_body={
                "starts": "1 3 0 5 8 5",
                "ends": "2 4 6 7 9 9",
            },
            sample_out_body={
                "ends": "2 4 6 7 9 9",
                "result": "[[1, 2], [3, 4], [5, 7], [8, 9]]",
                "starts": "1 3 0 5 8 5",
            },
            py_code="""
def act_select(starts, ends):
    class Activity:
        def __init__(self, s, f):
            self.s = s
            self.f = f
    
        def to_tuple(self):
            return self.s, self.f
    
        def __lt__(self, other):
            return self.f < other.f
    
    activities = []
    n = len(starts)
    for i in range(n):
        activities.append(Activity(starts[i], ends[i]))
    activities.sort()
    
    out = []
    i = 0
    out.append(activities[i])
    for j in range(1, n):
        if activities[j].s >= activities[i].f:
            out.append(activities[j])
            i = j
    return json.dumps([a.to_tuple() for a in out])
            """,
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Huffman Code",
            method="POST",
            endpoint=prog_root + "/huffman-code",
            description="Huffman coding is a lossless data compression algorithm.",
            theory="The idea is to assign variable-length codes to input characters, lengths of the assigned codes are \
based on the frequencies of corresponding characters. The most frequent character gets the smallest code and the least \
frequent character gets the largest code. The variable-length codes assigned to input characters are Prefix Codes, \
means the codes (bit sequences) are assigned in such a way that the code assigned to one character is not the prefix \
of code assigned to any other character.",
            inp_body=[
                ReqponseBodyItem(
                    key="inp",
                    desc="input string",
                    types=[ReqponseBodyItem.TYPE_STR],
                ),
            ],
            out_body=[
                ReqponseBodyItem(
                    key="input",
                    desc="input string",
                    types=[ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    key="result string",
                    desc="huffman code (output)",
                    types=[ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    key="individual_codes",
                    desc="map of each character and its code",
                    types=[ReqponseBodyItem.TYPE_MAP],
                ),
                ReqponseBodyItem(
                    key="error", desc="error message", types=[ReqponseBodyItem.TYPE_STR]
                ),
            ],
            sample_inp_body={"inp": "BCAADDDCCACACAC"},
            sample_out_body={
                "individual_codes": {"A": "11", "B": "100", "C": "0", "D": "101"},
                "input": "BCAADDDCCACACAC",
                "result": "1000111110110110100110110110",
            },
            py_code="""
def huffman_code(inp)
    class NodeTree(object):
        def __init__(self, left=None, right=None):
            self.left = left
            self.right = right
    
        def children(self):
            return self.left, self.right
    
        def nodes(self):
            return self.left, self.right
    
        def __str__(self):
            return "%s_%s" % (self.left, self.right)
    
    def huffman_code_tree(_node, bin_string=""):
        if type(_node) is str:
            return {_node: bin_string}
        (l, r) = _node.children()
        d = dict()
        d.update(huffman_code_tree(l, bin_string + "0"))
        d.update(huffman_code_tree(r, bin_string + "1"))
        return d
    
    freq = {}
    for c in inp:
        if c in freq.keys():
            freq[c] += 1
        else:
            freq[c] = 1
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    nodes = freq
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))
    
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    huffman_code = huffman_code_tree(nodes[0][0])
    out = ""
    for c in inp:
        out += huffman_code[c]
    return out
            """,
        ),
    ]
    category = "Dynamic Programming"
    data += []
    return data
