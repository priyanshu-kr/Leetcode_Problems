from typing import List

nums = [2,3,4,7,8,10,11,12,13]
target = 9

class Solution:
    def twoSums(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,n in enumerate(nums):
            req_n = target - n
            if req_n in seen:
                return [seen[req_n], i]
            else:
                seen[n] = i
        return []

sol = Solution()
print(sol.twoSums(nums, target))