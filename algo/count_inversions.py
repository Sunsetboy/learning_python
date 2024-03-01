import unittest

def merge_sort_and_count_inversions(unsorted_list):
    list_size = len(unsorted_list)
    if list_size < 2:
        return 0, unsorted_list
    
    print(f"sorting list: {unsorted_list}")

    left_list = unsorted_list[:list_size//2]
    right_list = unsorted_list[list_size//2:]

    left_inversions, left_list_sorted = merge_sort_and_count_inversions(left_list)
    right_inversions, right_list_sorted = merge_sort_and_count_inversions(right_list)
    cross_inversions, sorted_merged_list = merge_sorted(left_list_sorted, right_list_sorted)

    return (left_inversions + right_inversions + cross_inversions, sorted_merged_list)


def merge_sorted(list1, list2):
    inversions = 0
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i]<list2[j]:
            result.append(list1[i])
            i+=1
        else:
            result.append(list2[j])
            j += 1
            inversions += len(list1)-i
    while i < len(list1):
        result.append(list1[i])
        i+=1
    while j < len(list2):
        result.append(list2[j])
        j+=1
    print(f"merged {list1} and {list2} with {inversions} inversions")
    return (inversions, result)

def main():
    unsorted_array = [5, 4, 3, 2, 1]
    inversions, sorted = merge_sort_and_count_inversions(unsorted_array)

    print(inversions)

class Test(unittest.TestCase):
    def test_1(self):
        inversions, sorted = merge_sort_and_count_inversions([5, 4, 3, 2, 1])
        assert inversions == 10
        print("PASSED: inversions for [5, 4, 3, 2, 1] should be 10")

    def test_2(self):
        inversions, sorted = merge_sort_and_count_inversions([2, 4, 1, 3, 5])
        assert inversions == 3
        print("PASSED: inversions for [2, 4, 1, 3, 5] should be 3")


if __name__ == "__main__":
    unittest.main(verbosity=2)