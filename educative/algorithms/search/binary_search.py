import unittest

'''
Returns the position of the element with specified value or None
'''
def binary_search(arr: list, val):
    if len(arr) == 0:
        return None

    left=0
    right = len(arr) - 1
    while right >= left:
        mid = left + (right-left)//2
        if arr[mid] == val:
            return mid
        if arr[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    
    return None


class TestBinarySearch(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(binary_search([], 6), None)

    def test_existing(self):
        self.assertEqual(binary_search([1,2,5,6,8,13,55], 6), 3)
        
    def test_existing_left(self):
        self.assertEqual(binary_search([1,2,5,6,8,13,55], 1), 0)

    def test_existing_right(self):
        self.assertEqual(binary_search([1,2,5,6,8,13,55], 55), 6)
    
    def test_not_existing_small(self):
        self.assertEqual(binary_search([1,2,5,6,8,13,55], 0), None)
    
    def test_not_existing_large(self):
        self.assertEqual(binary_search([1,2,5,6,8,13,55], 100), None)



if __name__ == '__main__':
    unittest.main()