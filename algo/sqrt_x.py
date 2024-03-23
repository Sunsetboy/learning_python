"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

"""
import math

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x // 2

        while left <= right:
            middle = math.floor((right-left)/2 + left)
            if middle**2 == x:
                return middle
            if middle**2 < x and (middle+1)**2 > x:
                return middle
            if middle**2 > x:
                right = middle - 1
            elif middle**2 < x:
                left = middle + 1
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(4))
    print(solution.mySqrt(8))