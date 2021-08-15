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


class PrefixInfixPostfix:
    @staticmethod
    def is_operator(c):
        if (
            c == "*"
            or c == "+"
            or c == "-"
            or c == "/"
            or c == "^"
            or c == "("
            or c == ")"
        ):
            return True
        else:
            return False

    @staticmethod
    def infix_to_prefix(expr):
        expr = expr.split()
        precedence = {"/": 3, "*": 3, "+": 2, "-": 2, "^": 4, "(": 1}
        op_stack = Stack()
        prefix_list = []
        temp = []
        for token in expr:
            if str(token).isalnum():
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
        return " ".join(prefix_list)

    @staticmethod
    def infix_to_postfix(expr):
        expr = expr.split()
        precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
        op_stack = Stack()
        postfix_list = []
        for token in expr:
            if str(token).isalnum():
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

    @staticmethod
    def prefix_to_infix(expr):
        expr = expr.split()
        stack = []
        i = len(expr) - 1
        while i >= 0:
            if not PrefixInfixPostfix.is_operator(expr[i]):
                stack.append(expr[i])
                i -= 1
            else:
                s = f"( {stack.pop()} {expr[i]} {stack.pop()} )"
                stack.append(s)
                i -= 1

        return stack.pop()

    @staticmethod
    def postfix_to_infix(expr):
        expr = expr.split()
        s = []
        for i in expr:
            if i.isalnum():
                s.insert(0, i)
            else:
                op1 = s[0]
                s.pop(0)
                op2 = s[0]
                s.pop(0)
                s.insert(0, f"( {op2} {i} {op1} )")
        return s[0]
