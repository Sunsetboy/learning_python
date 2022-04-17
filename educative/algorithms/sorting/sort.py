import unittest


def find_smallest(arr: list) -> int:
    smallest = arr[0]
    smallest_index = 0

    for i in range(0, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort(arr: list) -> list:
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))

    return newArr


def quick_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


class TestSort(unittest.TestCase):

    def test_empty_array_quick(self):
        self.assertEqual(quick_sort([]), [])

    def test_empty_array_selection(self):
        self.assertEqual(selection_sort([]), [])

    def test_selection(self):
        self.assertEqual(selection_sort([5, 2, 1, 6, 8, 100, 55]), [
                         1, 2, 5, 6, 8, 55, 100])

    def test_quick(self):
        self.assertEqual(quick_sort([5, 2, 1, 6, 8, 100, 55]), [
                         1, 2, 5, 6, 8, 55, 100])

    def test_quick_empty(self):
        self.assertEqual([], quick_sort([]))


if __name__ == '__main__':
    unittest.main()
