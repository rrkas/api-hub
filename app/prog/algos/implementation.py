from datetime import datetime

from app.prog.models import *


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
        try:
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
        except BaseException as e:
            print(e)
            return "infix_to_prefix: " + str(e), True
        return " ".join(prefix_list), False

    @staticmethod
    def infix_to_postfix(expr):
        expr = expr.split()
        precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
        op_stack = Stack()
        postfix_list = []
        try:
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
        except BaseException as e:
            print(e)
            return "infix_to_postfix: " + str(e), True
        return " ".join(postfix_list), False

    @staticmethod
    def prefix_to_infix(expr):
        expr = expr.split()
        stack = []
        i = len(expr) - 1
        try:
            while i >= 0:
                if not PrefixInfixPostfix.is_operator(expr[i]):
                    stack.append(expr[i])
                    i -= 1
                else:
                    s = f"( {stack.pop()} {expr[i]} {stack.pop()} )"
                    stack.append(s)
                    i -= 1
        except BaseException as e:
            print(e)
            return "prefix_to_infix: " + str(e), True

        return stack.pop(), False

    @staticmethod
    def postfix_to_infix(expr):
        expr = expr.split()
        s = []
        try:
            for i in expr:
                if i.isalnum():
                    s.insert(0, i)
                else:
                    op1 = s[0]
                    s.pop(0)
                    op2 = s[0]
                    s.pop(0)
                    s.insert(0, f"( {op2} {i} {op1} )")
        except BaseException as e:
            print(e)
            return "postfix_to_infix: " + str(e), True

        return s[0], False

    @staticmethod
    def evaluate_prefix(expr):
        expr = expr.split()
        stack = []
        try:
            for c in expr[::-1]:
                c = str(c)
                if c.isdigit():
                    stack.append(int(c))
                elif c.isalpha():
                    return "evaluate_prefix: only numbers allowed", True
                else:
                    o1 = stack.pop()
                    o2 = stack.pop()
                    if c == "+":
                        stack.append(o1 + o2)
                    elif c == "-":
                        stack.append(o1 - o2)
                    elif c == "*":
                        stack.append(o1 * o2)
                    elif c == "/":
                        stack.append(o1 / o2)
        except BaseException as e:
            print(e)
            return "evaluate_prefix: " + str(e), True
        return stack.pop(), False

    @staticmethod
    def evaluate_postfix(expr):
        expr = expr.split()
        stack = Stack()
        try:
            for i in expr:
                if i.isdigit():
                    stack.push(i)
                else:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.push(str(eval(val2 + i + val1)))
            res = int(stack.pop())
        except BaseException as e:
            print(e)
            return "evaluate_postfix: " + str(e), True
        return res, False


class Sort:
    @staticmethod
    def bubble_sort(inp):
        sort = ProgSort()
        sort.inp = inp
        inp = inp[:]
        start = datetime.now()
        # start

        n = len(inp)
        for i in range(n):
            for j in range(0, n - i - 1):
                if inp[j] > inp[j + 1]:
                    inp[j], inp[j + 1] = inp[j + 1], inp[j]
        # end
        end = datetime.now()
        sort.result = inp
        sort.time_taken = (start - end).microseconds // 1000
        return sort

    @staticmethod
    def insertion_sort(inp):
        sort = ProgSort()
        sort.inp = inp
        inp = inp[:]
        start = datetime.now()
        # start

        for i in range(1, len(inp)):
            key = inp[i]
            j = i - 1
            while j >= 0 and key < inp[j]:
                inp[j + 1] = inp[j]
                j -= 1
            inp[j + 1] = key

        # end
        end = datetime.now()
        sort.result = inp
        sort.time_taken = (start - end).microseconds // 1000
        return sort

    @staticmethod
    def selection_sort(inp):
        sort = ProgSort()
        sort.inp = inp
        inp = inp[:]
        start = datetime.now()
        # start

        for i in range(len(inp)):
            min_idx = i
            for j in range(i + 1, len(inp)):
                if inp[min_idx] > inp[j]:
                    min_idx = j
            inp[i], inp[min_idx] = inp[min_idx], inp[i]

        # end
        end = datetime.now()
        sort.result = inp
        sort.time_taken = (start - end).microseconds // 1000
        return sort

    @staticmethod
    def merge_sort(inp):
        sort = ProgSort()
        sort.inp = inp
        inp = inp[:]
        start = datetime.now()

        # start

        def merge(arr, l, m, r):
            n1, n2 = m - l + 1, r - m
            L, R = arr[l : l + n1], arr[m + 1 : m + 1 + n2]
            i, j, k = 0, 0, l
            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1
            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1

        def mergeSort(arr, l, r):
            if l < r:
                m = l + (r - l) // 2
                mergeSort(arr, l, m)
                mergeSort(arr, m + 1, r)
                merge(arr, l, m, r)

        mergeSort(inp, 0, len(inp) - 1)

        # end
        end = datetime.now()
        sort.result = inp
        sort.time_taken = (start - end).microseconds // 1000
        return sort

    @staticmethod
    def quick_sort(inp):
        sort = ProgSort()
        sort.inp = inp
        inp = inp[:]
        start = datetime.now()

        # start

        def partition(array, low, high):
            pivot = array[high]
            i = low - 1
            for j in range(low, high):
                if array[j] <= pivot:
                    i = i + 1
                    array[i], array[j] = array[j], array[i]
            array[i + 1], array[high] = array[high], array[i + 1]
            return i + 1

        def quickSort(array, low, high):
            if low < high:
                pi = partition(array, low, high)
                quickSort(array, low, pi - 1)
                quickSort(array, pi + 1, high)

        quickSort(inp, 0, len(inp) - 1)

        # end
        end = datetime.now()
        sort.result = inp
        sort.time_taken = (start - end).microseconds // 1000
        return sort