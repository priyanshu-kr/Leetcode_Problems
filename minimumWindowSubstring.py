'''
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:
m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.
'''

s = "ADOBECODEBANC"
t = "ABC"
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = {}
        for i in t:
            need[i] = need.get(i, 0) + 1
        
        window = {}
        have = 0
        need_count = len(need)
        
        L = 0
        min_len = float('inf')
        min_start = 0

        for R in range(0, len(s)):
            window[s[R]] = window.get(s[R], 0) + 1

            if s[R] in need and window[s[R]] == need[s[R]]:
                have += 1
            
            while have == need_count:
                current_len = R - L + 1

                if current_len < min_len:
                    min_len = current_len
                    min_start = L
                
                char = s[L]

                if char in need and window[char] == need[char]:
                    have -= 1
                
                window[char] -= 1
                L += 1

        if min_len == float('inf'):
            return ""
        else:
            return s[min_start : min_start + min_len]        

sol = Solution()
print(sol.minWindow(s, t))