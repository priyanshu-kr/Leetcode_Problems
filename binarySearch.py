from typing import List

nums = [-1, 0, 1, 4, 5, 18, 20]
target = 5

class Solution:
    def search(self, nums:List[int], target:int) -> int:
        
        left, right = 0, len(nums)-1
    
        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
                
sol = Solution()
print(sol.search(nums, target))