from flask import request

from app.prog.routes import prog_bp, prog_root
from . import PrefixInfixPostfix, Documentation, ReqponseBodyItem
from ...util import get_value_form_json


@prog_bp.route(prog_root + "/infix-to-prefix", methods=["POST"])
def prog_infix_to_prefix():
    expr_key = "expr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    expr = get_value_form_json(expr_key)
    if not expr.isalnum() and " " not in expr:
        return {"error": "please separate tokens using spaces!"}
    res, err = PrefixInfixPostfix.infix_to_prefix(expr)
    if err:
        return {"expr": expr, "error": res}
    return {"expr": expr, "result": res}


@prog_bp.route(prog_root + "/infix-to-postfix", methods=["POST"])
def prog_infix_to_postfix():
    expr_key = "expr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    expr = get_value_form_json(expr_key)
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


@prog_bp.route(prog_root + "/prefix-to-infix", methods=["POST"])
def prog_prefix_to_infix():
    expr_key = "expr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    expr = get_value_form_json(expr_key)
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


@prog_bp.route(prog_root + "/postfix-to-infix", methods=["POST"])
def prog_postfix_to_infix():
    expr_key = "expr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    expr = get_value_form_json(expr_key)
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


@prog_bp.route(prog_root + "/prefix-to-postfix", methods=["POST"])
def prog_prefix_to_postfix():
    expr_key = "expr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    expr = get_value_form_json(expr_key)
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
    expr = get_value_form_json(expr_key)
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
    expr = get_value_form_json(expr_key)
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
    expr = get_value_form_json(expr_key)
    if " " not in expr:
        return {"error": "please separate tokens using spaces!"}
    res, err = PrefixInfixPostfix.evaluate_postfix(expr)
    if err:
        return {"expr": expr, "error": res}
    return {
        "expr": expr,
        "result": res,
    }


def pre_in_post_docs():
    docs = []
    category = "Prefix-Infix-Postfix"
    docs.append(
        Documentation(
            category=category,
            name="Infix to Prefix",
            method="POST",
            endpoint=prog_root + "/infix-to-prefix",
            sample_request_url=prog_root + "/infix-to-prefix",
            description="Converts infix expression to prefix expression",
            inp_body=[
                ReqponseBodyItem(
                    "expr",
                    "infix expression (input)",
                    [ReqponseBodyItem.TYPE_STR],
                )
            ],
            out_body=[
                ReqponseBodyItem(
                    "expr",
                    "infix expression (input)",
                    [ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    "error",
                    "error message",
                    [ReqponseBodyItem.TYPE_STR],
                    optional=True,
                ),
                ReqponseBodyItem(
                    "result", "prefix expression (output)", [ReqponseBodyItem.TYPE_STR]
                ),
            ],
            sample_inp_body={"expr": "( 2 + 3 ) * 4"},
            sample_out_body={"expr": "( 2 + 3 ) * 4", "result": "* + 2 3 4"},
            args=None,
        )
    )
    docs.append(
        Documentation(
            category=category,
            name="Infix to Postfix",
            method="POST",
            endpoint=prog_root + "/infix-to-postfix",
            sample_request_url=prog_root + "/infix-to-postfix",
            description="Converts infix expression to postfix expression",
            inp_body=[
                ReqponseBodyItem(
                    "expr", "infix expression (input)", [ReqponseBodyItem.TYPE_STR]
                ),
            ],
            out_body=[
                ReqponseBodyItem(
                    "expr", "infix expression (input)", [ReqponseBodyItem.TYPE_STR]
                ),
                ReqponseBodyItem(
                    "error",
                    "error message",
                    [ReqponseBodyItem.TYPE_STR],
                    optional=True,
                ),
                ReqponseBodyItem(
                    "result", "postfix expression (output)", [ReqponseBodyItem.TYPE_STR]
                ),
            ],
            sample_inp_body={"expr": "( 2 + 3 ) * 4"},
            sample_out_body={"expr": "( 2 + 3 ) * 4", "result": "2 3 + 4 *"},
            args=None,
        )
    )
    docs.append(
        Documentation(
            category=category,
            name="Prefix to Infix",
            method="POST",
            endpoint=prog_root + "/prefix-to-infix",
            sample_request_url=prog_root + "/prefix-to-infix",
            description="Converts prefix expression to infix expression",
            inp_body=[
                ReqponseBodyItem(
                    "expr", "prefix expression (input)", [ReqponseBodyItem.TYPE_STR]
                )
            ],
            out_body=[
                ReqponseBodyItem(
                    "expr", "prefix expression (input)", [ReqponseBodyItem.TYPE_STR]
                ),
                ReqponseBodyItem(
                    "error",
                    "error message",
                    [ReqponseBodyItem.TYPE_STR],
                    optional=True,
                ),
                ReqponseBodyItem(
                    "result", "infix expression (output)", [ReqponseBodyItem.TYPE_STR]
                ),
            ],
            sample_inp_body={"expr": "* + 2 3 45"},
            sample_out_body={"expr": "* + 2 3 45", "result": "( ( 2 + 3 ) * 45 )"},
            args=None,
        )
    )
    docs.append(
        Documentation(
            category=category,
            name="Postfix to Infix",
            method="POST",
            endpoint=prog_root + "/postfix-to-infix",
            sample_request_url=prog_root + "/postfix-to-infix",
            description="Converts postfix expression to infix expression",
            inp_body=[
                ReqponseBodyItem(
                    "expr",
                    "postfix expression (input)",
                    [ReqponseBodyItem.TYPE_STR],
                )
            ],
            out_body=[
                ReqponseBodyItem(
                    "expr", "postfix expression (input)", [ReqponseBodyItem.TYPE_STR]
                ),
                ReqponseBodyItem(
                    "error", "error message", [ReqponseBodyItem.TYPE_STR], optional=True
                ),
                ReqponseBodyItem(
                    "result", "infix expression (output)", [ReqponseBodyItem.TYPE_STR]
                ),
            ],
            sample_inp_body={"expr": "2 3 + 45 *"},
            sample_out_body={"expr": "2 3 + 45 *", "result": "( ( 2 + 3 ) * 45 )"},
            args=None,
        )
    )
    docs.append(
        Documentation(
            category=category,
            name="Prefix to Postfix",
            method="POST",
            endpoint=prog_root + "/prefix-to-postfix",
            sample_request_url=prog_root + "/prefix-to-postfix",
            description="Converts prefix expression to postfix expression",
            inp_body=[
                ReqponseBodyItem(
                    "expr",
                    "prefix expression (input)",
                    [ReqponseBodyItem.TYPE_STR],
                )
            ],
            out_body=[
                ReqponseBodyItem(
                    "expr", "prefix expression (input)", [ReqponseBodyItem.TYPE_STR]
                ),
                ReqponseBodyItem(
                    "error",
                    "error message",
                    [ReqponseBodyItem.TYPE_STR],
                    optional=True,
                ),
                ReqponseBodyItem(
                    "result", "postfix expression (output)", [ReqponseBodyItem.TYPE_STR]
                ),
            ],
            sample_inp_body={"expr": "* + 2 3 45"},
            sample_out_body={"expr": "* + 2 3 45", "result": "2 3 + 45 *"},
            args=None,
        )
    )
    docs.append(
        Documentation(
            category=category,
            name="Postfix to Prefix",
            method="POST",
            endpoint=prog_root + "/postfix-to-prefix",
            sample_request_url=prog_root + "/postfix-to-prefix",
            description="Converts postfix expression to prefix expression",
            inp_body=[
                ReqponseBodyItem(
                    "expr",
                    "postfix expression (input)",
                    [ReqponseBodyItem.TYPE_STR],
                )
            ],
            out_body=[
                ReqponseBodyItem(
                    "expr",
                    "postfix expression (input)",
                    [ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    "error",
                    "error message",
                    [ReqponseBodyItem.TYPE_STR],
                    optional=True,
                ),
                ReqponseBodyItem(
                    "result",
                    "prefix expression (output)",
                    [ReqponseBodyItem.TYPE_STR],
                ),
            ],
            sample_inp_body={"expr": "2 3 + 45 *"},
            sample_out_body={
                "expr": "2 3 + 45 *",
                "result": "* + 2 3 45",
            },
            args=None,
        )
    )
    docs.append(
        Documentation(
            category=category,
            name="Evaluate Prefix",
            method="POST",
            endpoint=prog_root + "/evaluate-prefix",
            sample_request_url=prog_root + "/evaluate-prefix",
            description="Evaluates prefix expression",
            inp_body=[
                ReqponseBodyItem(
                    "expr",
                    "prefix expression (input)",
                    [ReqponseBodyItem.TYPE_STR],
                )
            ],
            out_body=[
                ReqponseBodyItem(
                    "expr",
                    "prefix expression (input)",
                    [ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    "error",
                    "error message",
                    [ReqponseBodyItem.TYPE_STR],
                    optional=True,
                ),
                ReqponseBodyItem(
                    "result",
                    "value (output)",
                    [ReqponseBodyItem.TYPE_FLOAT],
                ),
            ],
            sample_inp_body={"expr": "* + 2 3 45"},
            sample_out_body={
                "expr": "* + 2 3 45",
                "result": 225.0,
            },
            args=None,
        )
    )
    docs.append(
        Documentation(
            category=category,
            name="Evaluate Postfix",
            method="POST",
            endpoint=prog_root + "/evaluate-postfix",
            sample_request_url=prog_root + "/evaluate-postfix",
            description="Evaluates postfix expression",
            inp_body=[
                ReqponseBodyItem(
                    "expr",
                    "postfix expression (input)",
                    [ReqponseBodyItem.TYPE_STR],
                )
            ],
            out_body=[
                ReqponseBodyItem(
                    "expr",
                    "postfix expression (input)",
                    [ReqponseBodyItem.TYPE_STR],
                ),
                ReqponseBodyItem(
                    "error",
                    "error message",
                    [ReqponseBodyItem.TYPE_STR],
                    optional=True,
                ),
                ReqponseBodyItem(
                    "result",
                    "value (output)",
                    [ReqponseBodyItem.TYPE_FLOAT],
                ),
            ],
            sample_inp_body={"expr": "2 3 + 45 *"},
            sample_out_body={
                "expr": "2 3 + 45 *",
                "result": 225.0,
            },
            args=None,
        )
    )
    return docs
