'''
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
'''

from typing import List

heights = [2,1,5,6,2,3]

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            # Use a virtual bar of height 0 at the end (that's why n+1) 
            # in case of sth like [1,3,7] bcz we won't be able to pop 'bar of 7' as there is no lower bar further 
            
            if i == n:
                current_height = 0
            else:
                current_height = heights[i]

            while stack and current_height < heights[stack[-1]]:
                popped_index = stack.pop()
                rectangle_height = heights[popped_index]
                
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                
                area = rectangle_height * width
                max_area = max(area, max_area)
            
            if i < n:
                stack.append(i)

        return max_area

sol = Solution()
print(sol.largestRectangleArea(heights))