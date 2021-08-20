from flask import request

from app.prog.algos import BasicAlgorithms
from app.prog.routes import prog_bp, prog_root
from app.util import get_value_form_json


@prog_bp.route(prog_root + "/factorial", methods=["POST"])
def prog_factorial():
    expr_key = "inp"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    inp = get_value_form_json(expr_key)
    try:
        inp = int(inp)
        out, err = BasicAlgorithms.factorial(inp)
        if err:
            return {
                "inp": inp,
                "algo": "factorial",
                "error": out,
            }
    except BaseException as e:
        return {"error": str(e)}
    return {
        "inp": inp,
        "out": out,
        "algo": "factorial",
    }


@prog_bp.route(prog_root + "/factors", methods=["POST"])
def prog_factors():
    expr_key = "inp"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    inp = get_value_form_json(expr_key)
    try:
        inp = int(inp)
        out, err = BasicAlgorithms.factors(inp)
        if err:
            return {
                "inp": inp,
                "algo": "factors",
                "error": out,
            }
    except BaseException as e:
        return {"error": str(e)}
    return {
        "inp": inp,
        "out": out,
        "algo": "factors",
    }


@prog_bp.route(prog_root + "/fibonacci", methods=["POST"])
def prog_fibonacci():
    expr_key = "inp"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    inp = get_value_form_json(expr_key)
    try:
        inp = int(inp)
        out, err = BasicAlgorithms.fibonacci(inp)
        if err:
            return {
                "inp": inp,
                "algo": "factors",
                "error": out,
            }
    except BaseException as e:
        return {"error": str(e)}
    return {
        "inp": inp,
        "out": out,
        "algo": "factors",
    }
