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
    subject = "Programming"
    category = "Prefix-Infix-Postfix"
    return [
        Documentation(
            subject=subject,
            category=category,
            name="Infix to Prefix",
            method="POST",
            endpoint=prog_root + "/infix-to-prefix",
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
                ),
                ReqponseBodyItem(
                    "result", "prefix expression (output)", [ReqponseBodyItem.TYPE_STR]
                ),
            ],
            sample_inp_body={"expr": "( 2 + 3 ) * 4"},
            sample_out_body={"expr": "( 2 + 3 ) * 4", "result": "* + 2 3 4"},
            args=None,
            steps=[
                "Reverse the infix expression given in the problem.",
                "Scan the expression from left to right.",
                "Whenever the operands arrive, print them.",
                "If the operator arrives and the stack is found to be empty, \
then simply push the operator into the stack.",
                "If the incoming operator has higher precedence than the TOP of the stack, \
push the incoming operator into the stack.",
                "If the incoming operator has the same precedence with a TOP of the stack, \
push the incoming operator into the stack.",
                "If the incoming operator has lower precedence than the TOP of the stack, pop, and \
print the top of the stack. Test the incoming operator against the top of the stack again and \
pop the operator from the stack till it finds the operator of a lower precedence or same precedence.",
                "If the incoming operator has the same precedence with the top of the stack and \
the incoming operator is ^, then pop the top of the stack till the condition is true. \
If the condition is not true, push the ^ operator.",
                "When we reach the end of the expression, pop, and print all the operators from the top of the stack.",
                "If the operator is ')', then push it into the stack.",
                "If the operator is '(', then pop all the operators from the stack till it finds ')' \
opening bracket in the stack.",
                "If the top of the stack is ')', push the operator on the stack.",
                "Reverse the output.",
            ],
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Infix to Postfix",
            method="POST",
            endpoint=prog_root + "/infix-to-postfix",
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
                ),
                ReqponseBodyItem(
                    "result", "postfix expression (output)", [ReqponseBodyItem.TYPE_STR]
                ),
            ],
            sample_inp_body={"expr": "( 2 + 3 ) * 4"},
            sample_out_body={"expr": "( 2 + 3 ) * 4", "result": "2 3 + 4 *"},
            args=None,
            steps=[
                "Initialize the Stack.",
                "Scan the operator from left to right in the infix expression.",
                "If the leftmost character is an operand, set it as the current output to the Postfix string.",
                "And if the scanned character is the operator and the Stack is empty or contains the '(', ')' \
symbol, push the operator into the Stack.",
                "If the scanned operator has higher precedence than the existing precedence operator in the \
Stack or if the Stack is empty, put it on the Stack.",
                "If the scanned operator has lower precedence than the existing operator in the Stack, \
pop all the Stack operators. After that, push the scanned operator into the Stack.",
                "If the scanned character is a left bracket '(', push it into the Stack.",
                "If we encountered right bracket ')', pop the Stack and print all output string character until \
'(' is encountered and discard both the bracket.",
                "Repeat all steps from 2 to 8 until the infix expression is scanned.",
                "Print the Stack output.",
                "Pop and output all characters, including the operator, from the Stack until it is not empty.",
            ],
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Prefix to Infix",
            method="POST",
            endpoint=prog_root + "/prefix-to-infix",
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
                ),
                ReqponseBodyItem(
                    "result", "infix expression (output)", [ReqponseBodyItem.TYPE_STR]
                ),
            ],
            sample_inp_body={"expr": "* + 2 3 45"},
            sample_out_body={"expr": "* + 2 3 45", "result": "( ( 2 + 3 ) * 45 )"},
            args=None,
            steps=[
                "Read the Prefix expression in reverse order (from right to left)",
                "If the symbol is an operand, then push it onto the Stack",
                "If the symbol is an operator, then pop two operands from the Stack",
                "Create a string by concatenating the two operands and the operator between them.",
                "string = (operand1 + operator + operand2)",
                "And push the resultant string back to Stack",
                "Repeat the above steps until end of Prefix expression.",
            ],
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Postfix to Infix",
            method="POST",
            endpoint=prog_root + "/postfix-to-infix",
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
            steps=[
                "If a character is operand, push it to stack.",
                "If a character is an operator, pop operand from the stack, say it’s s1, pop operand from the stack, \
say it’s s2, perform (s2 operator s1) and push it to stack."
                "Once the expression iteration is completed, initialize the result string and pop out from the stack \
and add it to the result.",
                "Return the result.",
            ],
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Prefix to Postfix",
            method="POST",
            endpoint=prog_root + "/prefix-to-postfix",
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
                ),
                ReqponseBodyItem(
                    "result", "postfix expression (output)", [ReqponseBodyItem.TYPE_STR]
                ),
            ],
            sample_inp_body={"expr": "* + 2 3 45"},
            sample_out_body={"expr": "* + 2 3 45", "result": "2 3 + 45 *"},
            args=None,
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Postfix to Prefix",
            method="POST",
            endpoint=prog_root + "/postfix-to-prefix",
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
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Evaluate Prefix",
            method="POST",
            endpoint=prog_root + "/evaluate-prefix",
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
            steps=[
                "Put a pointer P at the end of the end",
                "If character at P is an operand push it to Stack",
                "If the character at P is an operator pop two elements from the Stack. Operate on these elements \
according to the operator, and push the result back to the Stack",
                "Decrement P by 1 and go to Step 2 as long as there are characters left to be scanned \
in the expression.",
                "The Result is stored at the top of the Stack, return it",
                "End",
            ],
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Evaluate Postfix",
            method="POST",
            endpoint=prog_root + "/evaluate-postfix",
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
            steps=[
                "Create a stack to store operands (or values).",
                "Scan the given expression and do following for every scanned element. If the element is a number, \
push it into the stack. If the element is a operator, pop operands for the operator from stack. Evaluate the operator \
and push the result back to the stack ",
                "When the expression is ended, the number in the stack is the final answer.",
            ],
        ),
    ]
