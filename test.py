import unittest
from selection_sort import selection_sort

class TestSortingAlgos(unittest.TestCase):
    def test_selection_sort(self):
        # Test case with unsorted integers
        arr = [9, 4, 2, 7, 5, 1, 8, 3, 6]
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(selection_sort(arr), expected_result)

    def test_selection_sort_empty(self):
        # Test case with an empty list
        arr = []
        expected_result = []
        self.assertEqual(selection_sort(arr), expected_result)
    
    def test_selection_sort_already_sorted(self):
        # Test case with already sorted list
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(selection_sort(arr), expected_result)

    def test_selection_sort_duplicate_values(self):
        # Test case with duplicate values
        arr = [3, 1, 2, 2, 4, 3, 4, 1]
        expected_result = [1, 1, 2, 2, 3, 3, 4, 4]
        self.assertEqual(selection_sort(arr), expected_result)

if __name__ == '__main__':
    unittest.main()