from typing import List

nums = [-1, 0, 1, 4, 5, 18, 20]
target = 18

class Solution:
    def binarySearch(self, nums:List[int], left:int, right:int, target:int) -> int:
        
        if left > right:
            return -1
        
        mid = (left + right)//2

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self.binarySearch(nums, left, mid-1, target)
        else:
            return self.binarySearch(nums, mid+1, right, target)
        
    def search(self, nums:List[int], target:int) -> int:
        return self.binarySearch(nums, 0, len(nums)-1, target)

sol = Solution()
print(sol.search(nums, target))