from typing import List

strs = [""]

class Solution:
    def longestCommonPrefix(self, strs:List[str]) -> str:

        short = min(len(s) for s in strs)
        result = ""

        for i in range(0, short):
            char = strs[0][i]
            for s in strs[1:]:
                if s[i] != char:
                    return result 
            result += char
        return result

sol = Solution()
print(sol.longestCommonPrefix(strs))
