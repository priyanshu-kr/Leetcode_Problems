'''
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
'''

from typing import List

matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]
target = 30

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        L = 0
        R = m * n - 1

        while L <= R:
            mid = (L + R) // 2
            r = mid // n
            c = mid % n
            value = matrix[r][c]

            if value == target:
                return True
            elif value < target:
                L = mid + 1
            else:
                R = mid - 1

        return False

sol = Solution()
print(sol.searchMatrix(matrix, target))