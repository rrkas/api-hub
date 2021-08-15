class Stack:
    def __init__(self):
        self.a = []

    def is_empty(self):
        return self.a == []

    def push(self, i):
        self.a.append(i)

    def pop(self):
        return self.a.pop()

    def peek(self):
        return self.a[len(self.a) - 1]

    def __repr__(self):
        return str(self.a)


def infix_to_prefix(s):
    precedence = {"/": 3, "*": 3, "+": 2, "-": 2, "^": 4, "(": 1}
    op_stack = Stack()
    prefix_list = []
    temp = []
    for token in s:
        if (
            token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            or token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
            or token in "0123456789"
        ):
            prefix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                temp.append(top_token)
                top_token = op_stack.pop()
            prefix_list = temp + prefix_list
            temp = []
        else:
            while (not op_stack.is_empty()) and (
                precedence[op_stack.peek()] >= precedence[token]
            ):
                temp.append(op_stack.pop())
            prefix_list = temp + prefix_list
            temp = []
            op_stack.push(token)
    while not op_stack.is_empty():
        temp.append(op_stack.pop())
    prefix_list = temp + prefix_list
    return "".join(prefix_list)


def infix_to_postfix(expr):
    precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    op_stack = Stack()
    postfix_list = []
    token_list = expr.split()

    for token in token_list:
        if (
            token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            or token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
            or token in "0123456789"
        ):
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (
                precedence[op_stack.peek()] >= precedence[token]
            ):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)
