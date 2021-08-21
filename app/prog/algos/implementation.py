from datetime import datetime

from app.models import *


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
                try:
                    stack.append(float(c))
                except:
                    if c.isalpha():
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
            res = float(stack.pop())
        except BaseException as e:
            print(e)
            return "evaluate_postfix: " + str(e), True
        return res, False


class Sort:
    @staticmethod
    def bubble_sort(inp):
        sort = ProgSort()
        sort.algo = "Bubble Sort"
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
        sort.algo = "Insertion Sort"
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
        sort.algo = "Selection Sort"
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
        sort.algo = "Merge Sort"
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
        sort.algo = "Quick Sort"
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

    @staticmethod
    def counting_sort(inp):
        sort = ProgSort()
        sort.algo = "Counting Sort"
        sort.inp = inp
        inp = inp[:]
        start = datetime.now()

        # start

        def countingSort(array):
            size = len(array)
            output = [0] * size
            count = [0] * (max(array) + 2)
            for i in array:
                count[i] += 1
            for i in range(1, len(count)):
                count[i] += count[i - 1]
            i = size - 1
            while i >= 0:
                output[count[array[i]] - 1] = array[i]
                count[array[i]] -= 1
                i -= 1
            for i in range(size):
                array[i] = output[i]

        countingSort(inp)

        # end
        end = datetime.now()
        sort.result = inp
        sort.time_taken = (start - end).microseconds // 1000
        return sort

    @staticmethod
    def radix_sort(inp):
        sort = ProgSort()
        sort.algo = "Radix Sort"
        sort.inp = inp
        inp = inp[:]
        start = datetime.now()

        # start

        def countingSort(array, place):
            size = len(array)
            output = [0] * size
            count = [0] * 10
            for i in range(0, size):
                index = array[i] // place
                count[index % 10] += 1
            for i in range(1, 10):
                count[i] += count[i - 1]
            i = size - 1
            while i >= 0:
                index = array[i] // place
                output[count[index % 10] - 1] = array[i]
                count[index % 10] -= 1
                i -= 1
            for i in range(0, size):
                array[i] = output[i]

        def radixSort(array):
            max_element = max(array)
            place = 1
            while max_element // place > 0:
                countingSort(array, place)
                place *= 10

        radixSort(inp)

        # end
        end = datetime.now()
        sort.result = inp
        sort.time_taken = (start - end).microseconds // 1000
        return sort

    @staticmethod
    def bucket_sort(inp):
        sort = ProgSort()
        sort.algo = "Bucket Sort"
        sort.inp = inp
        inp = inp[:]
        start = datetime.now()

        # start

        def insertionSort(b):
            for i in range(1, len(b)):
                up = b[i]
                j = i - 1
                while j >= 0 and b[j] > up:
                    b[j + 1] = b[j]
                    j -= 1
                b[j + 1] = up
            return b

        def bucketSort(x):
            arr = []
            slot_num = 10
            for i in range(slot_num):
                arr.append([])
            for j in x:
                index_b = int(slot_num * j)
                arr[index_b].append(j)
            for i in range(slot_num):
                arr[i] = insertionSort(arr[i])
            k = 0
            for i in range(slot_num):
                for j in range(len(arr[i])):
                    x[k] = arr[i][j]
                    k += 1
            return x

        bucketSort(inp)

        # end
        end = datetime.now()
        sort.result = inp
        sort.time_taken = (start - end).microseconds // 1000
        return sort

    @staticmethod
    def heap_sort(inp):
        sort = ProgSort()
        sort.algo = "Heap Sort"
        sort.inp = inp
        inp = inp[:]
        start = datetime.now()

        # start

        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[i] < arr[l]:
                largest = l
            if r < n and arr[largest] < arr[r]:
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        def heapSort(arr):
            n = len(arr)
            for i in range(n // 2, -1, -1):
                heapify(arr, n, i)
            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                heapify(arr, i, 0)

        heapSort(inp)

        # end
        end = datetime.now()
        sort.result = inp
        sort.time_taken = (start - end).microseconds // 1000
        return sort

    @staticmethod
    def shell_sort(inp):
        sort = ProgSort()
        sort.algo = "Shell Sort"
        sort.inp = inp
        inp = inp[:]
        start = datetime.now()

        # start

        def shellSort(array):
            n = len(array)
            interval = n // 2
            while interval > 0:
                for i in range(interval, n):
                    temp = array[i]
                    j = i
                    while j >= interval and array[j - interval] > temp:
                        array[j] = array[j - interval]
                        j -= interval
                    array[j] = temp
                interval //= 2

        shellSort(inp)

        # end
        end = datetime.now()
        sort.result = inp
        sort.time_taken = (start - end).microseconds // 1000
        return sort


class Search:
    @staticmethod
    def linear_search(arr, x):
        search = ProgSearch()
        search.algo = "Linear Search"
        search.inp = arr
        search.key = x
        start = datetime.now()
        # start

        for i in range(len(arr)):
            if arr[i] == x:
                search.result = i
                break

        # end
        end = datetime.now()
        search.comparisons = search.result + 1 if search.result > -1 else len(arr)
        search.time_taken = (start - end).microseconds // 1000
        return search

    @staticmethod
    def binary_search(arr, x):
        search = ProgSearch()
        search.algo = "Binary Search"
        search.inp = arr
        search.key = x
        start = datetime.now()

        # start
        def binarySearch(arr, l, r, x):
            if r >= l:
                search.comparisons += 1
                mid = l + (r - l) // 2
                if arr[mid] == x:
                    search.comparisons += 1
                    return mid
                elif arr[mid] > x:
                    return binarySearch(arr, l, mid - 1, x)
                else:
                    return binarySearch(arr, mid + 1, r, x)
            else:
                return -1

        search.result = binarySearch(arr, 0, len(arr) - 1, x)

        # end
        end = datetime.now()
        search.time_taken = (start - end).microseconds // 1000
        return search


class BasicAlgorithms:
    @staticmethod
    def factorial(n):
        if n < 0:
            return "factorial of negative is undefined!", True
        if n > 2_00_000:
            return "input bigger than 100,000!", True
        try:
            f = 1
            for i in range(1, n + 1):
                f *= i
            return f, False
        except BaseException as e:
            return str(e), True

    @staticmethod
    def factors(n):
        if n < 0:
            return "factors of negative is undefined", True
        try:
            s = []
            for i in range(1, n + 1):
                if n % i == 0:
                    s.append(i)
            s = list(map(str, s))
            return " ".join(s), False
        except BaseException as e:
            return str(e), True

    @staticmethod
    def fibonacci(n):
        if n < 1:
            return "input less than 1!", True
        try:
            if n == 1:
                return 0, False
            elif n in [2, 3]:
                return 1, False
            else:
                a = 0
                b = 1
                c = 0
                for _ in range(2, n):
                    c = a + b
                    a, b = b, c
                return c, False
        except BaseException as e:
            return str(e), True

    @staticmethod
    def palindrome(n):
        try:
            return n == n[::-1], False
        except BaseException as e:
            return str(e), True

    @staticmethod
    def strong_number(n):
        if n < 0:
            return "input less than 0!", True
        try:
            s = 0
            t = n
            while t > 0:
                d = t % 10
                s += BasicAlgorithms.factorial(d)[0]
                t //= 10
            return s == n, False
        except BaseException as e:
            return str(e), True

    @staticmethod
    def armstrong_number(n):
        """Armstrong number is a number that is equal to the sum of cubes of its digits"""
        if n < 0:
            return "input less than 0!", True
        try:
            s = 0
            t = n
            while t > 0:
                d = t % 10
                s += d ** 3
                t //= 10
            return s == n, False
        except BaseException as e:
            return str(e), True


class AdvancedAlgorithms:

    # greedy algos
    @staticmethod
    def fractional_knapsack(weighs, vals, capacity):
        if capacity < 0:
            return "capacity less than 0!", True
        elif capacity == 0:
            return 0, False
        elif any([w < 0 for w in weighs]) or any([v < 0 for v in vals]):
            return "one/more weight/value less than 0!", True
        elif len(weighs) != len(vals):
            return "number of weighs and values unequal!", True
        elif len(weighs) == 0:
            return 0, False

        if sum(weighs) <= capacity:
            return sum(vals), False

        class Item:
            def __init__(self, w, v, idx):
                self.w = w
                self.v = v
                self.idx = idx
                self.cost = v / w

            def __lt__(self, other):
                return self.cost < other.cost

        items = []
        for i in range(len(vals)):
            items.append(Item(weighs[i], vals[i], i))

        items.sort(reverse=True)

        total_value = 0
        for i in items:
            cur_wt = i.w
            cur_val = i.v
            if capacity - cur_wt >= 0:
                capacity -= cur_wt
                total_value += cur_val
            else:
                fraction = capacity / cur_wt
                total_value += cur_val * fraction
                break

        return total_value, False

    @staticmethod
    def activity_selection(starts, ends):
        if len(starts) != len(ends):
            return "start-end count mismatch!", True
        elif len(starts) == 0:
            return "empty lists!", True

        class Activity:
            def __init__(self, s, f):
                self.s = s
                self.f = f

            def to_tuple(self):
                return self.s, self.f

            def __lt__(self, other):
                return self.f < other.f

        activities = []
        n = len(starts)
        for i in range(n):
            activities.append(Activity(starts[i], ends[i]))
        activities.sort()

        out = []
        i = 0
        out.append(activities[i])
        for j in range(1, n):
            if activities[j].s >= activities[i].f:
                out.append(activities[j])
                i = j
        return [a.to_tuple() for a in out], False

    @staticmethod
    def job_sequencing(ids, deadlines, profits):
        pass
