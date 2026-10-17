'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
 
Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
'''
from typing import List

height = [0,1,0,2,1,0,1,3,2,1,2,1]

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        L = 0
        R = len(height) - 1

        left_max = 0
        right_max = 0

        while L < R:
            if height[L] <= height[R]:
                left_max = max(left_max, height[L])
                water += left_max - height[L]
                L += 1

            else:
                right_max = max(right_max, height[R])
                water += right_max - height[R]
                R -= 1

        return water

sol = Solution()
print(sol.trap(height))