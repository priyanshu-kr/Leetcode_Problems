'''
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
'''

from typing import List

nums = [100, 200, 1, 2, 4, 5, 3]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)

        """ if we want to see longest consecutive sequence separately (with storing it into separate set)"""
        # longest_seq = set()
        
        # for x in nums_set:
        #     if x-1 in nums_set:
        #         continue
            
        #     current_seq = {x}

        #     current = x

        #     while current+1 in nums_set:
        #         current += 1
        #         current_seq.add(current)

        #     if len(longest_seq) < len(current_seq):
        #         longest_seq = current_seq
        
        # print(longest_seq)
        # return len(longest_seq)

        """ if we want to see longest consecutive sequence separately (without storing it into separate set)"""
        # longest_len = 0
        # longest_start = None
        # longest_end = None

        # for x in nums_set:
        #     if x-1 in nums_set:
        #         continue

        #     current_len = 1
        #     current = x

        #     while current+1 in nums_set:
        #         current_len += 1
        #         current +=1
            
        #     if current_len > longest_len:
        #         longest_start = x
        #         longest_end = current
        #         longest_len = current_len

        # print(list(range(longest_start, longest_end+1)))
        # return longest_len

        """if we don't want to see the longest consecutive sequence (as asked in question)"""
        longest_len = 0

        for x in nums_set:
            if x-1 in nums_set:
                continue
        
            current_len = 1
            current = x

            while current+1 in nums_set:
                current_len += 1
                current +=1
        
            longest_len = max(longest_len, current_len)

        return longest_len

sol = Solution()
print(sol.longestConsecutive(nums))