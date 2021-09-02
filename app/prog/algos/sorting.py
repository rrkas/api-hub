from flask import request

from app.prog.routes import prog_bp, prog_root
from . import Sort, Documentation, ReqponseItem, ComplexityAnalysis
from ...util import get_value_form_json


@prog_bp.route(prog_root + "/sort-bubble", methods=["POST"])
def prog_sort_bubble():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    data = {"arr": arr}
    if " " not in arr:
        data.update({"error": "please separate numbers using spaces!"})
        return data
    try:
        arr = list(map(int, arr.split()))
    except BaseException as e1:
        try:
            arr = list(map(float, arr.split()))
        except BaseException as e2:
            data.update({"error": str(e1) + "; " + str(e2)})
            return data
    res = Sort.bubble_sort(arr)
    return res.json()


@prog_bp.route(prog_root + "/sort-insertion", methods=["POST"])
def prog_sort_insertion():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    data = {"arr": arr}
    if " " not in arr:
        data.update({"error": "please separate numbers using spaces!"})
        return data
    try:
        arr = list(map(int, arr.split()))
    except BaseException as e1:
        try:
            arr = list(map(float, arr.split()))
        except BaseException as e2:
            data.update({"error": str(e1) + "; " + str(e2)})
            return data
    res = Sort.insertion_sort(arr)
    return res.json()


@prog_bp.route(prog_root + "/sort-selection", methods=["POST"])
def prog_sort_selection():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    data = {"arr": arr}
    if " " not in arr:
        data.update({"error": "please separate numbers using spaces!"})
        return data
    try:
        arr = list(map(int, arr.split()))
    except BaseException as e1:
        try:
            arr = list(map(float, arr.split()))
        except BaseException as e2:
            data.update({"error": str(e1) + "; " + str(e2)})
            return data
    res = Sort.selection_sort(arr)
    return res.json()


@prog_bp.route(prog_root + "/sort-merge", methods=["POST"])
def prog_sort_merge():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    data = {"arr": arr}
    if " " not in arr:
        data.update({"error": "please separate numbers using spaces!"})
        return data
    try:
        arr = list(map(int, arr.split()))
    except BaseException as e1:
        try:
            arr = list(map(float, arr.split()))
        except BaseException as e2:
            data.update({"error": str(e1) + "; " + str(e2)})
            return data
    res = Sort.merge_sort(arr)
    return res.json()


@prog_bp.route(prog_root + "/sort-quick", methods=["POST"])
def prog_sort_quick():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    data = {"arr": arr}
    if " " not in arr:
        data.update({"error": "please separate numbers using spaces!"})
        return data
    try:
        arr = list(map(int, arr.split()))
    except BaseException as e1:
        try:
            arr = list(map(float, arr.split()))
        except BaseException as e2:
            data.update({"error": str(e1) + "; " + str(e2)})
            return data
    res = Sort.quick_sort(arr)
    return res.json()


@prog_bp.route(prog_root + "/sort-counting", methods=["POST"])
def prog_sort_counting():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    data = {"arr": arr}
    if " " not in arr:
        data.update({"error": "please separate numbers using spaces!"})
        return data
    try:
        arr = list(map(int, arr.split()))
        for i in arr:
            if i < 0:
                raise Exception(f"Only non negative numbers accepted; got {i}")
    except BaseException as e1:
        data.update({"error": str(e1)})
        return data
    res = Sort.counting_sort(arr)
    return res.json()


@prog_bp.route(prog_root + "/sort-radix", methods=["POST"])
def prog_sort_radix():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    data = {"arr": arr}
    if " " not in arr:
        data.update({"error": "please separate numbers using spaces!"})
        return data
    try:
        arr = list(map(int, arr.split()))
        for i in arr:
            if i < 0:
                raise Exception(f"Only non negative numbers accepted; got {i}")
    except BaseException as e1:
        data.update({"error": str(e1)})
        return data
    res = Sort.radix_sort(arr)
    return res.json()


@prog_bp.route(prog_root + "/sort-bucket", methods=["POST"])
def prog_sort_bucket():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    data = {"arr": arr}
    if " " not in arr:
        data.update({"error": "please separate numbers using spaces!"})
        return data
    try:
        arr = list(map(float, arr.split()))
    except BaseException as e:
        data.update({"error": str(e)})
        return data
    res = Sort.bucket_sort(arr)
    return res.json()


@prog_bp.route(prog_root + "/sort-heap", methods=["POST"])
def prog_sort_heap():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    data = {"arr": arr}
    if " " not in arr:
        data.update({"error": "please separate numbers using spaces!"})
        return data
    try:
        arr = list(map(int, arr.split()))
    except BaseException as e1:
        try:
            arr = list(map(float, arr.split()))
        except BaseException as e2:
            data.update({"error": str(e1) + "; " + str(e2)})
            return data
    res = Sort.heap_sort(arr)
    return res.json()


@prog_bp.route(prog_root + "/sort-shell", methods=["POST"])
def prog_sort_shell():
    expr_key = "arr"
    if (
        expr_key not in request.form.keys()
        and expr_key not in (request.json or {}).keys()
    ):
        return {"error": f"{expr_key} missing in body!"}
    arr = get_value_form_json(expr_key)
    data = {"arr": arr}
    if " " not in arr:
        data.update({"error": "please separate numbers using spaces!"})
        return data
    try:
        arr = list(map(int, arr.split()))
    except BaseException as e1:
        try:
            arr = list(map(float, arr.split()))
        except BaseException as e2:
            data.update({"error": str(e1) + "; " + str(e2)})
            return data
    res = Sort.shell_sort(arr)
    return res.json()


def sorting_docs():
    subject = "Programming"
    category = "Sorting"
    return [
        Documentation(
            subject=subject,
            category=category,
            name="Bubble Sort",
            description="Sorts array of integers, float/double using bubble sort algorithm.",
            endpoint=prog_root + "/sort-bubble",
            args=None,
            method="POST",
            inp_body=[
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                )
            ],
            out_body=[
                ReqponseItem(
                    "algorithm", "name of algorithm used", [ReqponseItem.TYPE_STR]
                ),
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "result",
                    "space separated numbers (output)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "time_taken",
                    "time taken (milliseconds) to complete the algorithm",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "error",
                    "error message",
                    [ReqponseItem.TYPE_STR],
                ),
            ],
            sample_inp_body={
                "arr": "15 12 1 0 -8 9 4",
            },
            sample_out_body={
                "algorithm": "Bubble Sort",
                "arr": "15 12 1 0 -8 9 4",
                "result": "-8 0 1 4 9 12 15",
                "time_taken": "0 milliseconds",
            },
            theory="This sorting algorithm is comparison-based algorithm in which each pair of adjacent elements \
is compared and the elements are swapped if they are not in order.",
            py_code="""
n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    """,
            time_complexity=ComplexityAnalysis("n", "n*n", "n*n"),
            space_complexity=ComplexityAnalysis(1, 1, 1),
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Insertion Sort",
            description="Sorts array of integers, float/double using insertion sort algorithm.",
            endpoint=prog_root + "/sort-insertion",
            args=None,
            method="POST",
            inp_body=[
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                )
            ],
            out_body=[
                ReqponseItem(
                    "algorithm",
                    "name of algorithm used",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "result",
                    "space separated numbers (output)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "time_taken",
                    "time taken (milliseconds) to complete the algorithm",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "error",
                    "error message",
                    [ReqponseItem.TYPE_STR],
                ),
            ],
            sample_inp_body={
                "arr": "15 12 1 0 -8 9 4",
            },
            sample_out_body={
                "algorithm": "Insertion Sort",
                "arr": "15 12 1 0 -8 9 4",
                "result": "-8 0 1 4 9 12 15",
                "time_taken": "0 milliseconds",
            },
            theory="The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are \
picked and placed at the correct position in the sorted part.",
            py_code="""
for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
            """,
            time_complexity=ComplexityAnalysis("n", "n*n", "n*n"),
            space_complexity=ComplexityAnalysis(1, 1, 1),
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Selection Sort",
            description="Sorts array of integers, float/double using selection sort algorithm.",
            endpoint=prog_root + "/sort-selection",
            args=None,
            method="POST",
            inp_body=[
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                )
            ],
            out_body=[
                ReqponseItem(
                    "algorithm",
                    "name of algorithm used",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "result",
                    "space separated numbers (output)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "time_taken",
                    "time taken (milliseconds) to complete the algorithm",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "error",
                    "error message",
                    [ReqponseItem.TYPE_STR],
                ),
            ],
            sample_inp_body={
                "arr": "15 12 1 0 -8 9 4",
            },
            sample_out_body={
                "algorithm": "Selection Sort",
                "arr": "15 12 1 0 -8 9 4",
                "result": "-8 0 1 4 9 12 15",
                "time_taken": "0 milliseconds",
            },
            theory="The smallest element is selected from the unsorted array and swapped with the leftmost element, \
and that element becomes a part of the sorted array. This process continues moving unsorted array boundary by \
one element to the right.",
            py_code="""
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
                """,
            time_complexity=ComplexityAnalysis("n", "n*n", "n*n"),
            space_complexity=ComplexityAnalysis(1, 1, 1),
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Merge Sort",
            description="Sorts array of integers, float/double using merge sort algorithm.",
            endpoint=prog_root + "/sort-merge",
            args=None,
            method="POST",
            inp_body=[
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                )
            ],
            out_body=[
                ReqponseItem(
                    "algorithm",
                    "name of algorithm used",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "result",
                    "space separated numbers (output)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "time_taken",
                    "time taken (milliseconds) to complete the algorithm",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "error",
                    "error message",
                    [ReqponseItem.TYPE_STR],
                ),
            ],
            sample_inp_body={
                "arr": "15 12 1 0 -8 9 4",
            },
            sample_out_body={
                "algorithm": "Merge Sort",
                "arr": "15 12 1 0 -8 9 4",
                "result": "-8 0 1 4 9 12 15",
                "time_taken": "0 milliseconds",
            },
            theory="It works on the principle of Divide and Conquer. Merge sort repeatedly breaks down a list into \
several sublists until each sublist consists of a single element and merging those sublists in a manner \
that results into a sorted list.",
            py_code="""
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

mergeSort(arr, 0, len(arr) - 1)
                    """,
            time_complexity=ComplexityAnalysis("n*(log n)", "n*(log n)", "n*(log n)"),
            space_complexity=ComplexityAnalysis("n", "n", "n"),
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Quick Sort",
            description="Sorts array of integers, float/double using quick sort algorithm.",
            endpoint=prog_root + "/sort-quick",
            args=None,
            method="POST",
            inp_body=[
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                )
            ],
            out_body=[
                ReqponseItem(
                    "algorithm",
                    "name of algorithm used",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "result",
                    "space separated numbers (output)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "time_taken",
                    "time taken (milliseconds) to complete the algorithm",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "error",
                    "error message",
                    [ReqponseItem.TYPE_STR],
                ),
            ],
            sample_inp_body={
                "arr": "15 12 1 0 -8 9 4",
            },
            sample_out_body={
                "algorithm": "Quick Sort",
                "arr": "15 12 1 0 -8 9 4",
                "result": "-8 0 1 4 9 12 15",
                "time_taken": "0 milliseconds",
            },
            theory="Quick Sort is a sorting algorithm, which is commonly used in computer science. Quick Sort is a \
divide and conquer algorithm. It creates two empty arrays to hold elements less than the pivot value and elements \
greater than the pivot value, and then recursively sort the sub arrays.",
            py_code="""
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

quickSort(arr, 0, len(arr) - 1)

                    """,
            time_complexity=ComplexityAnalysis("n*(log n)", "n*(log n)", "n*n"),
            space_complexity=ComplexityAnalysis("log n", "log n", "log n"),
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Counting Sort",
            description="Sorts array of integers using counting sort algorithm.",
            endpoint=prog_root + "/sort-counting",
            args=None,
            method="POST",
            inp_body=[
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                )
            ],
            out_body=[
                ReqponseItem(
                    "algorithm",
                    "name of algorithm used",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "result",
                    "space separated numbers (output)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "time_taken",
                    "time taken (milliseconds) to complete the algorithm",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "error",
                    "error message",
                    [ReqponseItem.TYPE_STR],
                ),
            ],
            sample_inp_body={
                "arr": "15 12 1 0 8 9 4",
            },
            sample_out_body={
                "algorithm": "Counting Sort",
                "arr": "15 12 1 0 8 9 4",
                "result": "0 1 4 8 9 12 15",
                "time_taken": "0 milliseconds",
            },
            theory="Counting sort is a sorting technique based on keys between a specific range. It works by counting \
the number of objects having distinct key values (kind of hashing). Then doing some arithmetic to calculate the \
position of each object in the output sequence",
            py_code="""
def countingSort(array):
    size = len(array)
    output = [0] * size
    count = [0] * (max(array) + 1)
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

countingSort(arr)
            """,
            time_complexity=ComplexityAnalysis("n+k", "n+k", "n+k"),
            space_complexity=ComplexityAnalysis("max", "max", "max"),
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Radix Sort",
            description="Sorts array of integers using radix sort algorithm.",
            endpoint=prog_root + "/sort-radix",
            args=None,
            method="POST",
            inp_body=[
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                )
            ],
            out_body=[
                ReqponseItem(
                    "algorithm",
                    "name of algorithm used",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "result",
                    "space separated numbers (output)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "time_taken",
                    "time taken (milliseconds) to complete the algorithm",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "error",
                    "error message",
                    [ReqponseItem.TYPE_STR],
                ),
            ],
            sample_inp_body={
                "arr": "15 12 1 0 8 9 4",
            },
            sample_out_body={
                "algorithm": "Radix Sort",
                "arr": "15 12 1 0 8 9 4",
                "result": "0 1 4 8 9 12 15",
                "time_taken": "0 milliseconds",
            },
            theory="The idea of Radix Sort is to do digit by digit sort starting from least significant digit to most \
significant digit. Radix sort uses counting sort as a subroutine to sort.",
            py_code="""
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

radixSort(arr)
            """,
            time_complexity=ComplexityAnalysis("n+k", "n+k", "n+k"),
            space_complexity=ComplexityAnalysis("max", "max", "max"),
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Bucket Sort",
            description="Sorts array of float/double using bucket sort algorithm.",
            endpoint=prog_root + "/sort-bucket",
            args=None,
            method="POST",
            inp_body=[
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                )
            ],
            out_body=[
                ReqponseItem(
                    "algorithm",
                    "name of algorithm used",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "result",
                    "space separated numbers (output)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "time_taken",
                    "time taken (milliseconds) to complete the algorithm",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "error",
                    "error message",
                    [ReqponseItem.TYPE_STR],
                ),
            ],
            sample_inp_body={
                "arr": "15 12 1 0 8 9 4",
            },
            sample_out_body={
                "algorithm": "Radix Sort",
                "arr": "15 12 1 0 8 9 4",
                "result": "0 1 4 8 9 12 15",
                "time_taken": "0 milliseconds",
            },
            theory="Bucket sort, or bin sort, is a sorting algorithm that works by distributing the elements of an \
array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, \
or by recursively applying the bucket sorting algorithm.",
            py_code="""
def bucketSort(arr, noOfBuckets):
    max_ele = max(arr)
    min_ele = min(arr)
    slot_size = (max_ele - min_ele) / noOfBuckets
    temp = []
    for i in range(noOfBuckets):
        temp.append([])
    for i in range(len(arr)):
        diff = (arr[i] - min_ele) / slot_size - int((arr[i] - min_ele) / slot_size)
        if diff == 0 and arr[i] != min_ele:
            temp[int((arr[i] - min_ele) / slot_size) - 1].append(arr[i])
        else:
            temp[int((arr[i] - min_ele) / slot_size)].append(arr[i])
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                arr[k] = i
                k = k + 1

bucketSort(arr, 5)
            """,
            time_complexity=ComplexityAnalysis("n+k", "n+k", "n+k"),
            space_complexity=ComplexityAnalysis("max", "max", "max"),
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Heap Sort",
            description="Sorts array of integers, float/double using heap sort algorithm.",
            endpoint=prog_root + "/sort-heap",
            args=None,
            method="POST",
            inp_body=[
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                )
            ],
            out_body=[
                ReqponseItem(
                    "algorithm",
                    "name of algorithm used",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "result",
                    "space separated numbers (output)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "time_taken",
                    "time taken (milliseconds) to complete the algorithm",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "error",
                    "error message",
                    [ReqponseItem.TYPE_STR],
                ),
            ],
            sample_inp_body={
                "arr": "15 12 1 0 8 9 4",
            },
            sample_out_body={
                "algorithm": "Heap Sort",
                "arr": "15 12 1 0 8 9 4",
                "result": "0 1 4 8 9 12 15",
                "time_taken": "0 milliseconds",
            },
            theory="Heap sort is a comparison-based sorting technique based on Binary Heap data structure. It is \
similar to selection sort where we first find the minimum element and place the minimum element at the beginning. We \
repeat the same process for the remaining elements.",
            py_code="""
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

heapSort(arr)
            """,
            time_complexity=ComplexityAnalysis("n*(log n)", "n*(log n)", "n*(log n)"),
            space_complexity=ComplexityAnalysis(1, 1, 1),
        ),
        Documentation(
            subject=subject,
            category=category,
            name="Shell Sort",
            description="Sorts array of integers, float/double using heap sort algorithm.",
            endpoint=prog_root + "/sort-shell",
            args=None,
            method="POST",
            inp_body=[
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                )
            ],
            out_body=[
                ReqponseItem(
                    "algorithm",
                    "name of algorithm used",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "arr",
                    "space separated numbers (input)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "result",
                    "space separated numbers (output)",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "time_taken",
                    "time taken (milliseconds) to complete the algorithm",
                    [ReqponseItem.TYPE_STR],
                ),
                ReqponseItem(
                    "error",
                    "error message",
                    [ReqponseItem.TYPE_STR],
                ),
            ],
            sample_inp_body={
                "arr": "15 12 1 0 8 9 4",
            },
            sample_out_body={
                "algorithm": "Shell Sort",
                "arr": "15 12 1 0 8 9 4",
                "result": "0 1 4 8 9 12 15",
                "time_taken": "0 milliseconds",
            },
            theory="Shell sort is a generalized version of the insertion sort algorithm. It first sorts elements that \
are far apart from each other and successively reduces the interval between the elements to be sorted. The interval \
between the elements is reduced based on the sequence used.",
            py_code="""
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

shellSort(arr)
            """,
            time_complexity=ComplexityAnalysis("n*(log n)", "n*n", "n*(log n)"),
            space_complexity=ComplexityAnalysis(1, 1, 1),
        ),
    ]
