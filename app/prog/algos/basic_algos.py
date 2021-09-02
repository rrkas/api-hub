from flask import request

from app.prog.algos import (
    BasicAlgorithms,
    Documentation,
    ReqponseItem,
    ComplexityAnalysis,
)
from app.prog.routes import prog_bp, prog_root
from app.util import get_value_form_json


@prog_bp.route(prog_root + "/fibonacci", methods=["POST"])
def prog_fibonacci():
    algo = "Fibonacci"
    expr_key = "n"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    inp = get_value_form_json(expr_key)
    data = {
        "n": inp,
        "algo": algo,
    }
    try:
        inp = int(inp)
        data["n"] = inp
        out, err = BasicAlgorithms.fibonacci(inp)
        if err:
            data.update({"error": out})
            return data
    except BaseException as e:
        data.update({"error": str(e)})
        return data
    data.update({"out": out})
    return data


@prog_bp.route(prog_root + "/palindrome", methods=["POST"])
def prog_palindrome():
    algo = "Palindrome"
    expr_key = "inp"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    inp = get_value_form_json(expr_key)
    data = {
        "inp": inp,
        "algo": algo,
    }
    try:
        out, err = BasicAlgorithms.palindrome(inp)
        if err:
            data.update({"error": out})
            return data
    except BaseException as e:
        data.update({"error": str(e)})
        return data
    data.update({"out": out})
    return data


@prog_bp.route(prog_root + "/strong-number", methods=["POST"])
def prog_strong_number():
    algo = "Strong Number"
    expr_key = "n"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    inp = get_value_form_json(expr_key)
    data = {
        "n": inp,
        "algo": algo,
    }
    try:
        inp = int(inp)
        data["n"] = inp
        out, err = BasicAlgorithms.strong_number(inp)
        if err:
            data.update({"error": out})
            return data
    except BaseException as e:
        data.update({"error": str(e)})
        return data
    data.update({"out": out})
    return data


@prog_bp.route(prog_root + "/armstrong-number", methods=["POST"])
def prog_armstrong_number():
    algo = "Armstrong Number"
    expr_key = "n"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    inp = get_value_form_json(expr_key)
    data = {
        "n": inp,
        "algo": algo,
    }
    try:
        inp = int(inp)
        data["n"] = inp
        out, err = BasicAlgorithms.armstrong_number(inp)
        if err:
            data.update({"error": out})
            return data
    except BaseException as e:
        data.update({"error": str(e)})
        return data
    data.update({"out": out})
    return data


def basic_docs():
    subject = "Programming"
    category = "Basic Algorithms"
    return [
        Documentation(
            subject=subject,
            category=category,
            name="Fibonacci",
            endpoint=prog_root + "/fibonacci",
            method="POST",
            description="nth term of Fibonacci series.",
            inp_body=[
                ReqponseItem(
                    key="n",
                    desc="nth Fibonacci term",
                    types=[ReqponseItem.TYPE_INT],
                )
            ],
            out_body=[
                ReqponseItem(
                    key="n",
                    desc="Input number",
                    types=[ReqponseItem.TYPE_INT],
                ),
                ReqponseItem(
                    key="algo",
                    desc="Algo name",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="out",
                    desc="nth term (output)",
                    types=[ReqponseItem.TYPE_INT],
                ),
                ReqponseItem(
                    key="error",
                    desc="Error message",
                    types=[ReqponseItem.TYPE_STR],
                ),
            ],
            sample_inp_body={
                "n": 20,
            },
            sample_out_body={
                "algo": "Fibonacci",
                "n": 20,
                "out": 4181,
            },
            py_code="""
def fibo(n):
    if n == 1:
        return 0
    elif n in [2, 3]:
        return 1
    else:
        a = 0
        b = 1
        c = None
        for _ in range(2, n):
            c = a + b
            a, b = b, c
        return c
                    """,
            time_complexity=ComplexityAnalysis(1, "n", "n"),
            space_complexity=ComplexityAnalysis(1, 1, 1),
            theory="nth term = sum of previous 2 terms, where:\n1st term = 0\n2nd term = 1",
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Palindrome",
            endpoint=prog_root + "/palindrome",
            method="POST",
            description="Checks if an element is palindrome or not.",
            inp_body=[
                ReqponseItem(
                    key="inp",
                    desc="element",
                )
            ],
            out_body=[
                ReqponseItem(
                    key="inp",
                    desc="element (Input) (modified)",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="algo",
                    desc="Algo name",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="out", desc="result", types=[ReqponseItem.TYPE_BOOL]
                ),
                ReqponseItem(
                    key="error",
                    desc="Error message",
                    types=[ReqponseItem.TYPE_STR],
                ),
            ],
            sample_inp_body={
                "inp": 202,
            },
            sample_out_body={
                "algo": "Palindrome",
                "inp": "202",
                "out": True,
            },
            py_code="""
def palin(n):
    n = str(n)
    return n == n[::-1]
                    """,
            time_complexity=ComplexityAnalysis("n", "n", "n"),
            space_complexity=ComplexityAnalysis(1, 1, 1),
            theory="Element and its reverse are equal.",
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Strong Number",
            endpoint=prog_root + "/strong-number",
            method="POST",
            description="Checks if an element is strong number or not.",
            inp_body=[
                ReqponseItem(
                    key="n",
                    desc="number",
                    types=[ReqponseItem.TYPE_INT],
                )
            ],
            out_body=[
                ReqponseItem(
                    key="n",
                    desc="number (Input)",
                    types=[ReqponseItem.TYPE_INT],
                ),
                ReqponseItem(
                    key="algo",
                    desc="Algo name",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="out", desc="result", types=[ReqponseItem.TYPE_BOOL]
                ),
                ReqponseItem(
                    key="error",
                    desc="Error message",
                    types=[ReqponseItem.TYPE_STR],
                ),
            ],
            sample_inp_body={
                "n": 145,
            },
            sample_out_body={"algo": "Strong Number", "n": 145, "out": True},
            py_code="""
def is_strong(n):
    s = 0
    t = n
    while t > 0:
        d = t % 10
        f = 1
        for i in range(1, d + 1):
            f *= i
        s += f
        t //= 10
    return s == n
""",
            theory="""Sum of Factorial of digits of number = number itself.
Example: 145
1! + 4! + 5! 
= 1 + 24 + 120 
= 145
            """,
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Armstrong Number",
            endpoint=prog_root + "/armstrong-number",
            method="POST",
            description="Checks if an element is armstrong number or not.",
            inp_body=[
                ReqponseItem(
                    key="n",
                    desc="number",
                    types=[ReqponseItem.TYPE_INT],
                )
            ],
            out_body=[
                ReqponseItem(
                    key="n",
                    desc="number (Input)",
                    types=[ReqponseItem.TYPE_INT],
                ),
                ReqponseItem(
                    key="algo",
                    desc="Algo name",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="out", desc="result", types=[ReqponseItem.TYPE_BOOL]
                ),
                ReqponseItem(
                    key="error",
                    desc="Error message",
                    types=[ReqponseItem.TYPE_STR],
                ),
            ],
            sample_inp_body={
                "n": 153,
            },
            sample_out_body={
                "algo": "Armstrong Number",
                "n": 153,
                "out": True,
            },
            py_code="""
def is_armstrong(n):
    s = 0
    t = n
    while t > 0:
        d = t % 10
        s += d ** 3
        t //= 10
    return s == n
    """,
            theory="""Sum of Cube of digits of number = number itself.
Example: 153
1^3 + 5^3 + 3^3 
= 1 + 125 + 27
= 153
                """,
        ),
    ]
