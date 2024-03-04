import unittest

'''
Questions to the interviewer:
could array values be negative?
could values be outside of buckets?
what to do with values on borders?

There is a list of numbers, the number of buckets is given n=10, 
the width of the bucket is m=5. 
The array nums needs to be scattered among the buckets and 
display statistics of the numbers (how many in each bucket). 
1st bucket: numbers from 0 to 5, 2nd: 5-10, 3rd: 10-15. 
The width and quantity are specified by the input parameters.

Examples: 
ex.1 : (3, 5, [7, 5, 12]) => {(0,4): [], (5,9): [5,7], (10-15): [12]}
ex. 2: (3, 5, [0, 15]) => {(0,4): [0], (5,9): [], (10-15): [15]}
ex: 3: (1, 5, [7, 5, 12]) => {(0,4): [7, 5, 12]}
'''

'''
{(0, 4): [], (5, 9): [7,5], (10,14): [12]}

!!!
Ask ofr exmpales

!!!
Edges cases - wrtie down what interviwer responds

!!!
Approach: 
1. iterate over nums
2. conditon >= jkk
3. add to hasmap
Valid approach
# prompt interviewer - does it sound okay for you?

7 // 5 => 1
5 // 5 => 1
12 // 5 => 2

15 // 5 => 3 => 2
123 // 5 => 24 => 2

N: (N*m, N*m+m-1)

O(n)

(-3, 1), (2, 7)

-3//5 = 0

1 // 5 = 0

# Tests:
(3, 5, [7, 5, 12])
iter1:
7 // 1 =>  output {[], [1], []}
5 // 2 = >  output {[1], [1], []}
'''

def solution(input):
  buckets_number, bucket_size, nums, left_boundary = inputs
  
  def dispatch(buckets_number, bucket_size, nums, left_boundary):

    result = {(N*bucket_size + left_boundary, N*bucket_size+bucket_size-1 + left_boundary ):[] for N in range(buckets_number)}

    if buckets_number == 1:
      result[result.keys()[0]] = nums
      return result

    for num in nums:
      bucket_number = num // bucket_size
      if bucket_number >= buckets_number:
        bucket_number = buckets_number - 1

      key = (bucket_number*bucket_size+left_boundary, bucket_number*bucket_size+bucket_size-1+left_boundary)

      result[key].append(num)

    return result
    
  
  def dispatch_iter(buckets_number, bucket_size, nums):
    
    result = {(N*bucket_size, N*bucket_size+bucket_size-1):[] for N in range(buckets_number)}
    
    if buckets_number == 1:
    	result[result.keys()[0]] = [num for num in nums]
        return result
    
    for num in nums:
      bucket_number = num // bucket_size
      if bucket_number >= buckets_number:
        bucket_number = buckets_number - 1

      key = (bucket_number*bucket_size, bucket_number*bucket_size+bucket_size-1)

      result[key].append(num)

    return result
  
  run solution(input)
    
  
'''
def dispatch(n, m, nums):
    results = [0]*n
    for num in nums:
        bucket_number = num // m
        results[bucket_number] += 1
    return results

class BukcetTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(dispatch(3, 5, [7, 5, 12]), [0,2,1])

if __name__ == "__main__":
    unittest.main()