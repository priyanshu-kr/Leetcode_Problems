'''
239. Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


Example 2:
Input: nums = [1], k = 1
Output: [1]
 
Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
'''

# using MONOTONIC DEQUE data structure

from typing import List
from collections import deque

nums = [1,3,-1,-3,5,3,6,7]
k = 3

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = []

        # Deque stores indices, not actual values.
        # It maintains elements in decreasing order of their values.
        dq = deque()

        for i in range(len(nums)):

            # STEP 1: Remove expired indices from the front.
            # The current window starts at i - k + 1.
            windowStart = i - k + 1

            while dq and dq[0] < windowStart:
                dq.popleft()

            # STEP 2: Remove smaller elements from the back.
            # A newer and larger element makes older smaller
            # elements permanently irrelevant.
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()

            # STEP 3: Add the current index to the back.
            dq.append(i)

            # STEP 4: Once the first complete window is formed,
            # the front of the deque represents its maximum.
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
    
sol = Solution()
print(sol.maxSlidingWindow(nums, k))

'''
If we want to find minimum element from each window we can just change 'nums[i] > nums[dq[-1]]' to 'nums[i] < nums[dq[-1]]'
and data structure will be called monotonically increasing deque instead of monotonically decreasing deque
'''