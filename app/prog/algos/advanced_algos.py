from app.prog.algos import AdvancedAlgorithms, Documentation, ReqponseItem
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


@prog_bp.route(prog_root + "/knapsack-01", methods=["POST"])
def prog_knapsack_01():
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
    except BaseException as e:
        response["error"] = str(e)
        return response
    try:
        vals = list(map(int, vals.split()))
    except BaseException as e:
        response["error"] = str(e)
        return response
    try:
        capacity = int(capacity)
    except BaseException as e:
        response["error"] = str(e)
        return response
    response["capacity"] = capacity
    res, err = AdvancedAlgorithms.knapsack_01(weighs, vals, capacity)
    if err:
        response["error"] = res
    else:
        response["result"] = res
    return response


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
                ReqponseItem(
                    key="weighs",
                    desc="space separated weighs of items",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="vals",
                    desc="space separated values of items",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="capacity",
                    desc="capacity of the knapsack (bag)",
                    types=[ReqponseItem.TYPE_FLOAT],
                ),
            ],
            out_body=[
                ReqponseItem(
                    key="weighs",
                    desc="space separated weighs of items",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="vals",
                    desc="space separated values of items",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="capacity",
                    desc="capacity of the knapsack (bag)",
                    types=[ReqponseItem.TYPE_FLOAT],
                ),
                ReqponseItem(
                    key="result", desc="max value", types=[ReqponseItem.TYPE_FLOAT]
                ),
                ReqponseItem(
                    key="error", desc="error message", types=[ReqponseItem.TYPE_STR]
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
            description="The activity selection problem is a combinatorial optimization problem concerning the \
selection of non-conflicting activities to perform within a given time frame, given a set of activities each marked \
by a start time and finish time.",
            theory="""
1) Sort the activities according to their finishing time 
2) Select the first activity from the sorted array and print it. 
3) Do the following for the remaining activities in the sorted array. 
…….a) If the start time of this activity is greater than or equal to the finish time of the previously selected \
activity then select this activity and print it.
            """,
            inp_body=[
                ReqponseItem(
                    key="starts",
                    desc="space separated start time of activities",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="ends",
                    desc="space separated end time of activities",
                    types=[ReqponseItem.TYPE_STR],
                ),
            ],
            out_body=[
                ReqponseItem(
                    key="starts",
                    desc="space separated start time of activities",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="ends",
                    desc="space separated end time of activities",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="result",
                    desc="jsonified list of list of start and end times of optimized activities",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="error", desc="error message", types=[ReqponseItem.TYPE_STR]
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
                ReqponseItem(
                    key="inp",
                    desc="input string",
                    types=[ReqponseItem.TYPE_STR],
                ),
            ],
            out_body=[
                ReqponseItem(
                    key="input",
                    desc="input string",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="result string",
                    desc="huffman code (output)",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="individual_codes",
                    desc="map of each character and its code",
                    types=[ReqponseItem.TYPE_MAP],
                ),
                ReqponseItem(
                    key="error", desc="error message", types=[ReqponseItem.TYPE_STR]
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
    data += [
        Documentation(
            subject=subject,
            category=category,
            name="Longest Common Subsequence",
            method="POST",
            endpoint=prog_root + "/longest-common-subsequence",
            description="The longest common subsequence problem is the problem of finding the longest subsequence \
common to all sequences in a set of sequences. It differs from the longest common substring problem: unlike \
substrings, subsequences are not required to occupy consecutive positions within the original sequences.",
            inp_body=[
                ReqponseItem(
                    key="str1",
                    desc="string 1",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="str2",
                    desc="string 2",
                    types=[ReqponseItem.TYPE_STR],
                ),
            ],
            out_body=[
                ReqponseItem(
                    key="str1",
                    desc="string 1",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="str2",
                    desc="string 2",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="lcs",
                    desc="longest common subsequence",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="error",
                    desc="error message",
                    types=[ReqponseItem.TYPE_STR],
                ),
            ],
            sample_inp_body={"str1": "ACADB", "str2": "CBDA"},
            sample_out_body={"lcs": "CB", "str1": "ACADB", "str2": "CBDA"},
            py_code="""
def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    l = [[0 for _ in range(n + 1)] for __ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                l[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                l[i][j] = l[i - 1][j - 1] + 1
            else:
                l[i][j] = max(l[i - 1][j], l[i][j - 1])
    index = l[m][n]
    lcs_algo = [""] * (index + 1)
    lcs_algo[index] = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_algo[index - 1] = s1[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif l[i - 1][j] > l[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs_algo)
            """,
        ),
        Documentation(
            subject=subject,
            category=category,
            name="N-Queens",
            method="POST",
            endpoint=prog_root + "/n-queens",
            description="The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two \
        queens attack each other.",
            inp_body=[
                ReqponseItem(
                    key="n",
                    desc="side of chessboard/ number of queens",
                    types=[ReqponseItem.TYPE_INT],
                ),
            ],
            out_body=[
                ReqponseItem(
                    key="n",
                    desc="side of chessboard/ number of queens",
                    types=[ReqponseItem.TYPE_INT],
                ),
                ReqponseItem(
                    key="board",
                    desc="list of rows of solution (list of strings)",
                    types=[ReqponseItem.TYPE_LIST],
                ),
                ReqponseItem(
                    key="error",
                    desc="error message",
                    types=[ReqponseItem.TYPE_STR],
                ),
            ],
            sample_inp_body={"n": 5},
            sample_out_body={
                "board": [
                    "1 0 0 0 0",
                    "0 0 0 1 0",
                    "0 1 0 0 0",
                    "0 0 0 0 1",
                    "0 0 1 0 0",
                ],
                "n": 5,
            },
            py_code="""
def n_queen(n):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve_nq_util(board, col):
        if col >= n:
            return True
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                if solve_nq_util(board, col + 1):
                    return True
                board[i][col] = 0
        return False

    def format_board(board):
        b = []
        for l in board:
            l = map(str, l)
            b.append(" ".join(l))
        return b

    board = [[0 for _ in range(n)] for __ in range(n)]
    solve_nq_util(board, 0)
    return board
            """,
        ),
        Documentation(
            subject=subject,
            category=category,
            name="0-1 Knapsack",
            method="POST",
            endpoint=prog_root + "/knapsack-01",
            description="Given weights and values of n items, we need to put these items in a knapsack of capacity W \
to get the maximum total value in the knapsack. Note: an item can be taken fully or ignored.",
            theory="In the Dynamic programming we will work considering the same cases as mentioned in the recursive \
approach. In a DP[][] table let’s consider all the possible weights from ‘1’ to ‘W’ as the columns and weights that \
can be kept as the rows. The state DP[i][j] will denote maximum value of ‘j-weight’ considering all values from \
‘1 to ith’. So if we consider ‘wi’ (weight in ‘ith’ row) we can fill it in all columns which have ‘weight values > wi’.\
 Now two possibilities can take place: Fill ‘wi’ in the given column, Do not fill ‘wi’ in the given column. \
Now we have to take a maximum of these two possibilities, formally if we do not fill ‘ith’ weight in ‘jth’ column then \
DP[i][j] state will be same as DP[i-1][j] but if we fill the weight, DP[i][j] will be equal to the value of ‘wi’+ \
value of the column weighing ‘j-wi’ in the previous row. So we take the maximum of these two possibilities \
to fill the current state. ",
            inp_body=[
                ReqponseItem(
                    key="weighs",
                    desc="space separated weighs of items",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="vals",
                    desc="space separated values of items",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="capacity",
                    desc="capacity of the knapsack (bag)",
                    types=[ReqponseItem.TYPE_INT],
                ),
            ],
            out_body=[
                ReqponseItem(
                    key="weighs",
                    desc="space separated weighs of items",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="vals",
                    desc="space separated values of items",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="capacity",
                    desc="capacity of the knapsack (bag)",
                    types=[ReqponseItem.TYPE_INT],
                ),
                ReqponseItem(
                    key="result", desc="max value", types=[ReqponseItem.TYPE_INT]
                ),
                ReqponseItem(
                    key="error", desc="error message", types=[ReqponseItem.TYPE_STR]
                ),
            ],
            sample_inp_body={
                "weighs": "10 40 20 30",
                "vals": "60 40 100 120",
                "capacity": 50,
            },
            sample_out_body={
                "capacity": 50,
                "result": 220,
                "vals": "60 40 100 120",
                "weighs": "10 40 20 30",
            },
            py_code="""
def knapsack_01(weighs, vals, capacity):
    def knapSack(W, wt, val, n):
        K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif wt[i - 1] <= w:
                    K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
                else:
                    K[i][w] = K[i - 1][w]
        return K[n][W]
    return knapSack(capacity, weighs, vals, len(weighs))
            """,
        ),
    ]
    return data
