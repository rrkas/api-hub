from flask import request

from . import ComplexityAnalysis, BasicAlgorithms, Documentation, ReqponseItem
from .routes import math_bp, math_root
from ..util import get_value_form_json


@math_bp.route(math_root + "/factorial", methods=["POST"])
def prog_factorial():
    expr_key = "n"
    algo = "Factorial"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    inp = get_value_form_json(expr_key)
    data = {"n": inp, "algo": algo}
    try:
        inp = int(inp)
        data["n"] = inp
        out, err = BasicAlgorithms.factorial(inp)
        if err:
            data.update({"error": out})
            return data
    except BaseException as e:
        data.update({"error": str(e)})
        return data
    data.update({"out": out})
    return data


@math_bp.route(math_root + "/factors", methods=["POST"])
def prog_factors():
    expr_key = "n"
    algo = "Factors"
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
        out, err = BasicAlgorithms.factors(inp)
        if err:
            data.update({"error": out})
            return data
    except BaseException as e:
        data.update({"error": str(e)})
        return data
    data.update({"out": out})
    return data



def basic_docs():
    subject = "Mathematics"
    category = "Basic"
    return [
        Documentation(
            subject=subject,
            category=category,
            name="Factorial",
            endpoint=math_root + "/factorial",
            method="POST",
            description="Factorial of a non negative number.",
            inp_body=[
                ReqponseItem(
                    key="n",
                    desc="Input number",
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
                    desc="Factorial (output)",
                    types=[ReqponseItem.TYPE_INT],
                ),
                ReqponseItem(
                    key="error",
                    desc="Error message",
                    types=[ReqponseItem.TYPE_STR],
                ),
            ],
            sample_inp_body={
                "n": 5,
            },
            sample_out_body={"algo": "Factorial", "n": 5, "out": 120},
            py_code="""
    def fact(n):
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f
                """,
            time_complexity=ComplexityAnalysis("n", "n", "n"),
            space_complexity=ComplexityAnalysis(1, 1, 1),
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Factors",
            endpoint=math_root + "/factors",
            method="POST",
            description="Factorials of a positive number.",
            inp_body=[
                ReqponseItem(
                    key="n",
                    desc="Input number",
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
                    desc="Space separated factors (output)",
                    types=[ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    key="error",
                    desc="Error message",
                    types=[ReqponseItem.TYPE_STR],
                ),
            ],
            sample_inp_body={
                "n": 12,
            },
            sample_out_body={"algo": "Factors", "n": 12, "out": "1 2 3 4 6 12"},
            py_code="""
    def factors(n):
        s = []
        for i in range(1, n + 1):
            if n % i == 0:
                s.append(i)
        return s
                    """,
            time_complexity=ComplexityAnalysis("n", "n", "n"),
            space_complexity=ComplexityAnalysis("n", "n", "n"),
        ),

    ]