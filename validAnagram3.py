from typing import List

s = "rac🫠car"
t = "carrac😂"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
    
sol = Solution()
print(sol.isAnagram(s,t))

# TC = O(nlogn + mlogm)
# SC = O(1) or O(n+m) depending on the sorting algo used 