'''
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:
1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
'''

s1 = "ab"
s2 = "eidbaooo"
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = {}
        count2 = {}

        for i in s1:
            count1[i] = count1.get(i, 0) + 1

        for i in range(len(s1)):
            count2[s2[i]] = count2.get(s2[i], 0) + 1

        if count1 == count2:
            return True
        
        L = 0
        for R in range(len(s1), len(s2)):
            # print("ITR")
            # print(count2)
            count2[s2[L]] -= 1
            # print(count2)

            if count2[s2[L]] == 0:
                count2.pop(s2[L])
            
            # print(count2)
            L += 1

            count2[s2[R]] = count2.get(s2[R], 0) + 1
            # print(count2)

            if count1 == count2:
                return True
            
            pass
        
        return False

sol = Solution()
print(sol.checkInclusion(s1, s2))
     