"""
Unit Testing: Testing Search and Sort Algorithms

Practical unittest example that tests real algorithms (search and sort)
with setUp/tearDown, multiple assertion methods, and edge cases.

Topics covered:
- unittest.TestCase subclassing
- setUp() for test data preparation
- Test method naming (test_ prefix)
- Assertion methods (assertEqual, assertLessEqual, assertRaises)
- Running tests: python -m unittest or pytest

Based on concepts from Python-100-Days test files and ch07/testing materials.
"""

import unittest


# =============================================================================
# Functions Under Test
# =============================================================================

def sequential_search(items: list, target) -> int:
    """Linear search - returns index or -1."""
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1


def binary_search(items: list, target) -> int:
    """Binary search on sorted list - returns index or -1."""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if target > items[mid]:
            start = mid + 1
        elif target < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


def selection_sort(items: list) -> list:
    """Selection sort - returns new sorted list."""
    result = items[:]
    for i in range(len(result) - 1):
        min_idx = i
        for j in range(i + 1, len(result)):
            if result[j] < result[min_idx]:
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
    return result


def merge(left: list, right: list) -> list:
    """Merge two sorted lists into one sorted list."""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# =============================================================================
# Test Case 1: Search Algorithm Tests
# =============================================================================

class TestSearchAlgorithms(unittest.TestCase):
    """Tests for sequential and binary search."""

    def setUp(self):
        """Prepare test data - runs before EACH test method."""
        self.unsorted = [35, 97, 12, 68, 55, 73, 81, 40]
        self.sorted = [12, 35, 40, 55, 68, 73, 81, 97]

    def test_sequential_search_found(self):
        """Test sequential search finds existing elements."""
        self.assertEqual(0, sequential_search(self.unsorted, 35))
        self.assertEqual(2, sequential_search(self.unsorted, 12))
        self.assertEqual(6, sequential_search(self.unsorted, 81))
        self.assertEqual(7, sequential_search(self.unsorted, 40))

    def test_sequential_search_not_found(self):
        """Test sequential search returns -1 for missing elements."""
        self.assertEqual(-1, sequential_search(self.unsorted, 99))
        self.assertEqual(-1, sequential_search(self.unsorted, 7))

    def test_sequential_search_empty_list(self):
        """Test sequential search on empty list."""
        self.assertEqual(-1, sequential_search([], 42))

    def test_binary_search_found(self):
        """Test binary search finds elements in sorted list."""
        self.assertEqual(1, binary_search(self.sorted, 35))
        self.assertEqual(0, binary_search(self.sorted, 12))
        self.assertEqual(6, binary_search(self.sorted, 81))
        self.assertEqual(2, binary_search(self.sorted, 40))
        self.assertEqual(7, binary_search(self.sorted, 97))

    def test_binary_search_not_found(self):
        """Test binary search returns -1 for missing elements."""
        self.assertEqual(-1, binary_search(self.sorted, 7))
        self.assertEqual(-1, binary_search(self.sorted, 99))

    def test_binary_search_single_element(self):
        """Test binary search with single-element list."""
        self.assertEqual(0, binary_search([42], 42))
        self.assertEqual(-1, binary_search([42], 99))


# =============================================================================
# Test Case 2: Sort Algorithm Tests
# =============================================================================

class TestSortAlgorithms(unittest.TestCase):
    """Tests for sorting algorithms."""

    def setUp(self):
        self.data = [35, 97, 12, 68, 55, 73, 81, 40]
        self.expected = [12, 35, 40, 55, 68, 73, 81, 97]

    def test_selection_sort_correctness(self):
        """Test that selection sort produces correct order."""
        result = selection_sort(self.data)
        self.assertEqual(result, self.expected)

    def test_selection_sort_no_side_effects(self):
        """Test that original list is not modified."""
        original = self.data[:]
        selection_sort(self.data)
        self.assertEqual(self.data, original)

    def test_selection_sort_already_sorted(self):
        """Test sorting an already sorted list."""
        result = selection_sort(self.expected)
        self.assertEqual(result, self.expected)

    def test_selection_sort_reverse_sorted(self):
        """Test sorting a reverse-sorted list."""
        result = selection_sort([5, 4, 3, 2, 1])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_selection_sort_duplicates(self):
        """Test sorting with duplicate values."""
        result = selection_sort([3, 1, 4, 1, 5, 9, 2, 6, 5])
        for i in range(len(result) - 1):
            self.assertLessEqual(result[i], result[i + 1])

    def test_selection_sort_empty(self):
        """Test sorting empty list."""
        self.assertEqual(selection_sort([]), [])

    def test_selection_sort_single_element(self):
        """Test sorting single-element list."""
        self.assertEqual(selection_sort([42]), [42])


# =============================================================================
# Test Case 3: Merge Function Tests
# =============================================================================

class TestMerge(unittest.TestCase):
    """Tests for the merge helper function."""

    def test_merge_basic(self):
        """Test merging two sorted lists."""
        left = [12, 35, 68, 97]
        right = [40, 55, 73, 81]
        result = merge(left, right)
        for i in range(len(result) - 1):
            self.assertLessEqual(result[i], result[i + 1])

    def test_merge_preserves_length(self):
        """Test that merge output has correct length."""
        left = [1, 3, 5]
        right = [2, 4, 6]
        result = merge(left, right)
        self.assertEqual(len(result), len(left) + len(right))

    def test_merge_empty_left(self):
        """Test merging with empty left list."""
        self.assertEqual(merge([], [1, 2, 3]), [1, 2, 3])

    def test_merge_empty_right(self):
        """Test merging with empty right list."""
        self.assertEqual(merge([1, 2, 3], []), [1, 2, 3])

    def test_merge_both_empty(self):
        """Test merging two empty lists."""
        self.assertEqual(merge([], []), [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
