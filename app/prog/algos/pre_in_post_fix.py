from flask import request

from app.prog.routes import prog_bp, prog_root
from . import PrefixInfixPostfix


@prog_bp.route(prog_root + "/infix-to-prefix", methods=["GET", "POST"])
def prog_infix_to_prefix():
    if request.method == "POST":
        expr_key = "expr"
        if (
                expr_key not in request.form.keys()
                and expr_key not in (request.json or {}).keys()
        ):
            return {"error": f"{expr_key} missing in body!"}
        if expr_key in request.form.keys():
            expr = request.form.get(expr_key)
        else:
            expr = request.json[expr_key]
        if not expr.isalnum() and " " not in expr:
            return {"error": "please separate tokens using spaces!"}
        res, err = PrefixInfixPostfix.infix_to_prefix(expr)
        if err:
            return {"expr": expr, "error": res}
        return {"expr": expr, "result": res}
    return {
        "api-name": "infix-to-prefix",
        "methods": ["GET", "POST"],
        "sample request": {
            "method": "POST",
            "url": request.base_url,
            "headers": {"Content-Type": "application/json"},
            "body": {"expr": "( a + b ) ^ c"},
        },
        "note": "separate tokens using spaces",
    }


@prog_bp.route(prog_root + "/infix-to-postfix", methods=["GET", "POST"])
def prog_infix_to_postfix():
    if request.method == "POST":
        expr_key = "expr"
        if (
                expr_key not in request.form.keys()
                and expr_key not in (request.json or {}).keys()
        ):
            return {"error": f"{expr_key} missing in body!"}
        if expr_key in request.form.keys():
            expr = request.form.get(expr_key)
        else:
            expr = request.json[expr_key]
        if not expr.isalnum() and " " not in expr:
            return {"error": "please separate tokens using spaces!"}
        res, err = PrefixInfixPostfix.infix_to_postfix(expr)
        if err:
            return {
                "expr": expr,
                "error": res,
            }
        return {
            "expr": expr,
            "result": res,
        }
    return {
        "api-name": "infix-to-postfix",
        "methods": ["GET", "POST"],
        "sample request": {
            "method": "POST",
            "url": request.base_url,
            "headers": {"Content-Type": "application/json"},
            "body": {"expr": "( a + b ) ^ c"},
        },
        "note": "separate tokens using spaces",
    }


@prog_bp.route(prog_root + "/prefix-to-infix", methods=["GET", "POST"])
def prog_prefix_to_infix():
    if request.method == "POST":
        expr_key = "expr"
        if (
                expr_key not in request.form.keys()
                and expr_key not in (request.json or {}).keys()
        ):
            return {"error": f"{expr_key} missing in body!"}
        if expr_key in request.form.keys():
            expr = request.form.get(expr_key)
        else:
            expr = request.json[expr_key]
        if not expr.isalnum() and " " not in expr:
            return {"error": "please separate tokens using spaces!"}
        res, err = PrefixInfixPostfix.prefix_to_infix(expr)
        if err:
            return {
                "expr": expr,
                "error": res,
            }
        return {
            "expr": expr,
            "result": res,
        }
    return {
        "api-name": "prefix-to-infix",
        "methods": ["GET", "POST"],
        "sample request": {
            "method": "POST",
            "url": request.base_url,
            "headers": {"Content-Type": "application/json"},
            "body": {"expr": "* + a b c"},
        },
        "note": "separate tokens using spaces",
    }


@prog_bp.route(prog_root + "/postfix-to-infix", methods=["GET", "POST"])
def prog_postfix_to_infix():
    if request.method == "POST":
        expr_key = "expr"
        if (
                expr_key not in request.form.keys()
                and expr_key not in (request.json or {}).keys()
        ):
            return {"error": f"{expr_key} missing in body!"}
        if expr_key in request.form.keys():
            expr = request.form.get(expr_key)
        else:
            expr = request.json[expr_key]
        if not expr.isalnum() and " " not in expr:
            return {"error": "please separate tokens using spaces!"}
        res, err = PrefixInfixPostfix.postfix_to_infix(expr)
        if err:
            return {
                "expr": expr,
                "error": res,
            }
        return {
            "expr": expr,
            "result": res,
        }
    return {
        "api-name": "postfix-to-infix",
        "methods": ["GET", "POST"],
        "sample request": {
            "method": "POST",
            "url": request.base_url,
            "headers": {"Content-Type": "application/json"},
            "body": {"expr": "2 3 + 4 *"},
        },
        "note": "separate tokens using spaces",
    }


@prog_bp.route(prog_root + "/prefix-to-postfix", methods=["POST"])
def prog_prefix_to_postfix():
    expr_key = "expr"
    if (
            expr_key not in request.form.keys()
            and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    if expr_key in request.form.keys():
        expr = request.form.get(expr_key)
    else:
        expr = request.json[expr_key]
    if not expr.isalnum() and " " not in expr:
        return {"error": "please separate tokens using spaces!"}
    res, err = PrefixInfixPostfix.prefix_to_infix(expr)
    if err:
        return {
            "expr": expr,
            "error": res,
        }
    res, err = PrefixInfixPostfix.infix_to_postfix(res)
    if err:
        return {
            "expr": expr,
            "error": res,
        }
    return {
        "expr": expr,
        "result": res,
    }


@prog_bp.route(prog_root + "/postfix-to-prefix", methods=["POST"])
def prog_postfix_to_prefix():
    expr_key = "expr"
    if (
            expr_key not in request.form.keys()
            and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    if expr_key in request.form.keys():
        expr = request.form.get(expr_key)
    else:
        expr = request.json[expr_key]
    if not expr.isalnum() and " " not in expr:
        return {"error": "please separate tokens using spaces!"}
    res, err = PrefixInfixPostfix.postfix_to_infix(expr)
    if err:
        return {"expr": expr, "error": res}
    res, err = PrefixInfixPostfix.infix_to_prefix(res)
    if err:
        return {"expr": expr, "error": res}
    return {
        "expr": expr,
        "result": res,
    }


@prog_bp.route(prog_root + "/eval-prefix", methods=["POST"])
def prog_eval_prefix():
    expr_key = "expr"
    if (
            expr_key not in request.form.keys()
            and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    if expr_key in request.form.keys():
        expr = request.form.get(expr_key)
    else:
        expr = request.json[expr_key]
    if " " not in expr:
        return {"error": "please separate tokens using spaces!"}
    res, err = PrefixInfixPostfix.evaluate_prefix(expr)
    if err:
        return {"expr": expr, "error": res}
    return {
        "expr": expr,
        "result": res,
    }


@prog_bp.route(prog_root + "/eval-postfix", methods=["POST"])
def prog_eval_postfix():
    expr_key = "expr"
    if (
            expr_key not in request.form.keys()
            and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    if expr_key in request.form.keys():
        expr = request.form.get(expr_key)
    else:
        expr = request.json[expr_key]
    if " " not in expr:
        return {"error": "please separate tokens using spaces!"}
    res, err = PrefixInfixPostfix.evaluate_postfix(expr)
    if err:
        return {"expr": expr, "error": res}
    return {
        "expr": expr,
        "result": res,
    }
