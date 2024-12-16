import unittest


def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return qsort(left) + middle + qsort(right)


class TestQsort(unittest.TestCase):
    def test_0(self):
        self.assertEqual(qsort([]), [])

    def test_1(self):
        self.assertEqual(qsort([100]), [100])

    def test_2(self):
        self.assertEqual(qsort([1, 3, 5, 6, 9]), [1, 3, 5, 6, 9])

    def test_3(self):
        self.assertEqual(qsort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_4(self):
        self.assertEqual(qsort([6, 100, 22, 11, 59, 12, 45, 2]), [2, 6, 11, 12, 22, 45, 59, 100])

    def test_5(self):
        self.assertEqual(qsort([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_6(self):
        self.assertEqual(qsort([-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]), [-9, -6, -5, -5, -5, -4, -3, -3, -2, -1, -1])

    def test_7(self):
        self.assertEqual(qsort([3, -1, 4, 1, -5, 9, -2, 6, 5, 3, 5]), [-5, -2, -1, 1, 3, 3, 4, 5, 5, 6, 9])


if __name__ == '__main__':
    unittest.main()
