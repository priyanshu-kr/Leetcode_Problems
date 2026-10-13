'''
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.


Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
'''

s = "AABABBA"
k = 1

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L = 0
        max_frequency = 0
        result = 0

        for R in range(len(s)):

            count[s[R]] = count.get(s[R], 0) + 1

            max_frequency = max(max_frequency, count[s[R]])

            while (R - L + 1) - max_frequency > k:
                count[s[L]] -= 1
                L += 1
            
            result = max(result, R - L + 1)
        
        return result

sol = Solution()
print(sol.characterReplacement(s, k))