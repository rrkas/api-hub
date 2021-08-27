import unittest

from app.prog.algos.implementation import *


class TestImplementations(unittest.TestCase):

    # pre-in-post
    def test_infix_to_prefix(self):
        self.assertEqual(
            PrefixInfixPostfix.infix_to_prefix("( ( 2 + 3 ) * 4 )")[0], "* + 2 3 4"
        )

    def test_infix_to_postfix(self):
        self.assertEqual(
            PrefixInfixPostfix.infix_to_postfix("( ( 2 + 3 ) * 4 )")[0], "2 3 + 4 *"
        )

    def test_prefix_to_infix(self):
        self.assertEqual(
            PrefixInfixPostfix.prefix_to_infix("* + 2 3 45")[0], "( ( 2 + 3 ) * 45 )"
        )

    def test_postfix_to_infix(self):
        self.assertEqual(
            PrefixInfixPostfix.postfix_to_infix("2 3 + 45 *")[0], "( ( 2 + 3 ) * 45 )"
        )

    def test_evaluate_prefix(self):
        self.assertEqual(PrefixInfixPostfix.evaluate_prefix("* + 2 3 45")[0], 225)

    def test_evaluate_postfix(self):
        self.assertEqual(PrefixInfixPostfix.evaluate_postfix("2 3 + 45 *")[0], 225)

    # sorting
    def test_bubble_sort(self):
        arr = [4, 5, 1, 2, 3, 8, 6]
        res = Sort.bubble_sort(arr[:])
        arr.sort()
        self.assertEqual(res.result, arr)

    def test_insertion_sort(self):
        arr = [4, 5, 1, 2, 3, 8, 6]
        res = Sort.insertion_sort(arr[:])
        arr.sort()
        self.assertEqual(res.result, arr)

    def test_selection_sort(self):
        arr = [4, 5, 1, 2, 3, 8, 6]
        res = Sort.selection_sort(arr[:])
        arr.sort()
        self.assertEqual(res.result, arr)

    def test_merge_sort(self):
        arr = [4, 5, 1, 2, 3, 8, 6]
        res = Sort.merge_sort(arr[:])
        arr.sort()
        self.assertEqual(res.result, arr)

    def test_quick_sort(self):
        arr = [4, 5, 1, 2, 3, 8, 6]
        res = Sort.quick_sort(arr[:])
        arr.sort()
        self.assertEqual(res.result, arr)

    def test_counting_sort(self):
        arr = [4, 5, 1, 2, 3, 8, 6]
        res = Sort.counting_sort(arr[:])
        arr.sort()
        self.assertEqual(res.result, arr)

    def test_radix_sort(self):
        arr = [4, 5, 1, 2, 3, 8, 6]
        res = Sort.radix_sort(arr[:])
        arr.sort()
        self.assertEqual(res.result, arr)

    def test_bucket_sort(self):
        arr = [0.4, 0.5, 0.1, 0.2, 0.3, 0.8, 0.6]
        res = Sort.bucket_sort(arr[:])
        arr.sort()
        self.assertEqual(res.result, arr)

    def test_heap_sort(self):
        arr = [4, 5, 1, 2, 3, 8, 6]
        res = Sort.heap_sort(arr[:])
        arr.sort()
        self.assertEqual(res.result, arr)

    def test_shell_sort(self):
        arr = [4, 5, 1, 2, 3, 8, 6]
        res = Sort.shell_sort(arr[:])
        arr.sort()
        self.assertEqual(res.result, arr)

    def test_strong_number(self):
        self.assertEqual(BasicAlgorithms.strong_number(145)[0], True)

    def test_armstrong_number(self):
        self.assertEqual(BasicAlgorithms.armstrong_number(153)[0], True)

    def test_knapsack_fractional(self):
        self.assertAlmostEqual(
            AdvancedAlgorithms.knapsack_fractional(
                [10, 40, 20, 30], [60, 40, 100, 120], 50
            )[0],
            240,
        )

    def test_activity_selection(self):
        self.assertEqual(
            AdvancedAlgorithms.activity_selection(
                [1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]
            )[0],
            [(1, 2), (3, 4), (5, 7), (8, 9)],
        )


if __name__ == "__main__":
    unittest.main()
