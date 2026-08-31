from typing import List

nums = [1,2,3,1]

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        seen = set()
        
        for n in nums:
            
            if n in seen:
                return True
            
            seen.add(n)
        
        return False

sol = Solution()
print(sol.containsDuplicate(nums))