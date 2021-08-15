from app.prog.models import *


class ProgTheory:
    algos = [
        ProgAlgo(
            algo_name="Infix to Prefix",
            route_name="infix-to-prefix",
            steps=[
                "Reverse the infix expression given in the problem.",
                "Scan the expression from left to right.",
                "Whenever the operands arrive, print them.",
                "If the operator arrives and the stack is found to be empty, then simply push the operator into the stack.",
                "If the incoming operator has higher precedence than the TOP of the stack, push the incoming operator into the stack.",
                "If the incoming operator has the same precedence with a TOP of the stack, push the incoming operator into the stack.",
                "If the incoming operator has lower precedence than the TOP of the stack, pop, and print the top of the stack. Test the incoming operator against the top of the stack again and pop the operator from the stack till it finds the operator of a lower precedence or same precedence.",
                "If the incoming operator has the same precedence with the top of the stack and the incoming operator is ^, then pop the top of the stack till the condition is true. If the condition is not true, push the ^ operator.",
                "When we reach the end of the expression, pop, and print all the operators from the top of the stack.",
                "If the operator is ')', then push it into the stack.",
                "If the operator is '(', then pop all the operators from the stack till it finds ')' opening bracket in the stack.",
                "If the top of the stack is ')', push the operator on the stack.",
                "Reverse the output.",
            ],
        ),
        ProgAlgo(
            algo_name="Infix to Postfix",
            route_name="infix-to-postfix",
            steps=[
                "Initialize the Stack.",
                "Scan the operator from left to right in the infix expression.",
                "If the leftmost character is an operand, set it as the current output to the Postfix string.",
                "And if the scanned character is the operator and the Stack is empty or contains the '(', ')' symbol, push the operator into the Stack.",
                "If the scanned operator has higher precedence than the existing precedence operator in the Stack or if the Stack is empty, put it on the Stack.",
                "If the scanned operator has lower precedence than the existing operator in the Stack, pop all the Stack operators. After that, push the scanned operator into the Stack.",
                "If the scanned character is a left bracket '(', push it into the Stack.",
                "If we encountered right bracket ')', pop the Stack and print all output string character until '(' is encountered and discard both the bracket.",
                "Repeat all steps from 2 to 8 until the infix expression is scanned.",
                "Print the Stack output.",
                "Pop and output all characters, including the operator, from the Stack until it is not empty.",
            ],
        ),
        ProgAlgo(
            algo_name="Prefix to Infix",
            route_name="prefix-to-infix",
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
    ]

    @staticmethod
    def find_algo_by_route(route_name):
        algo = [a for a in ProgTheory.algos if a.route_name == route_name]
        if len(algo) > 0:
            return algo[0]
        return None
