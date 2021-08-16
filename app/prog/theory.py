from app.prog.models import *


class ProgTheory:
    algos = [
        # pre-in-post fix
        ProgAlgo(
            algo_name="Infix to Prefix",
            route_name="infix-to-prefix",
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
        ProgAlgo(
            algo_name="Infix to Postfix",
            route_name="infix-to-postfix",
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
        ProgAlgo(
            algo_name="Postfix to Infix",
            route_name="postfix-to-infix",
            steps=[
                "If a character is operand, push it to stack.",
                "If a character is an operator, pop operand from the stack, say it’s s1, pop operand from the stack, \
say it’s s2, perform (s2 operator s1) and push it to stack."
                "Once the expression iteration is completed, initialize the result string and pop out from the stack \
and add it to the result.",
                "Return the result.",
            ],
        ),
        ProgAlgo(
            algo_name="Evaluate Prefix",
            route_name="eval-prefix",
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
        ProgAlgo(
            algo_name="Evaluate Postfix",
            route_name="eval-postfix",
            steps=[
                "Create a stack to store operands (or values).",
                "Scan the given expression and do following for every scanned element. If the element is a number, \
push it into the stack. If the element is a operator, pop operands for the operator from stack. Evaluate the operator \
and push the result back to the stack ",
                "When the expression is ended, the number in the stack is the final answer.",
            ]
        ),
    ]

    @staticmethod
    def find_algo_by_route(route_name):
        algo = [a for a in ProgTheory.algos if a.route_name == route_name]
        if len(algo) > 0:
            return algo[0]
        return None
