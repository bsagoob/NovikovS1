import unittest

def quick_sort(array):
    """Реализация быстрой сортировки."""
    if len(array) <= 1:
        return array
    pivot = array[0]
    left = [x for x in array[1:] if x <= pivot]
    right = [x for x in array[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

class QuickSortTest(unittest.TestCase):
    def test_empty_array(self):
        """Проверка сортировки пустого массива."""
        self.assertEqual(quick_sort([]), [])

    def test_already_sorted_array(self):
        """Проверка сортировки уже отсортированного массива."""
        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reversed_array(self):
        """Проверка сортировки массива в обратном порядке."""
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_random_array(self):
        """Проверка сортировки случайного массива."""
        self.assertEqual(quick_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]), [1, 1, 2, 3, 3, 4, 5, 5, 6, 9])

if __name__ == '__main__':
    unittest.main()

