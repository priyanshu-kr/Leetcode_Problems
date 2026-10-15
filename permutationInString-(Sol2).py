'''
567. Permutation in String (Solution 2)

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
s2 = "eidboaooo"

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        count1 = [0] * 26  # Character frequencies in s1
        count2 = [0] * 26  # Character frequencies in the current window of s2

        # Build the frequency array for s1.
        for c in s1:
            count1[ord(c) - ord('a')] += 1

        # Initialize the first window of s2. Its length must equal len(s1).
        for i in range(len(s1)):
            count2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1

        # If all 26 frequencies match, the first window is a permutation.
        if matches == 26:
            return True

        # Update one character's frequency in the current window.
        # delta = -1 when removing a character; +1 when adding one.
        def update_count(idx, delta):
            nonlocal matches

            # If this character's frequencies currently match, changing count2 will make them temporarily mismatch.
            if count1[idx] == count2[idx]:
                matches -= 1

            # Apply the frequency change.
            count2[idx] += delta

            # If the frequencies now match again, count that match.
            if count1[idx] == count2[idx]:
                matches += 1

        # Slide the fixed-size window through s2.
        L = 0

        # R points to each new character entering the window.
        for R in range(len(s1), len(s2)):

            # Remove the character leaving the window.
            outgoing = ord(s2[L]) - ord('a')
            update_count(outgoing, -1)

            # Add the new character entering the window.
            incoming = ord(s2[R]) - ord('a')
            update_count(incoming, +1)

            # Move the left boundary forward.
            L += 1

            # All 26 frequencies match, so this window is a permutation.
            if matches == 26:
                return True

        # No window matched s1's character frequencies.
        return False

# **Complexity analysis**

# - **Time:** \(O(m+n)\), where \(m=\text{len}(s1)\) and \(n=\text{len}(s2)\). Building the frequency arrays takes \(O(m)\), and sliding the window takes \(O(n-m)\). The 26-character comparison is constant time.
# - **Auxiliary space:** \(O(1)\), because both frequency arrays always contain exactly 26 entries.

# **Remember the core invariant:** `matches` counts how many of the 26 character frequencies are equal between `s1` and the current window. When `matches == 26`, every frequency agrees, so the window is a permutation of `s1`.

# The key optimization is that we **update only the two frequencies that change** instead of comparing all 26 frequencies after every window movement.

sol = Solution()
print(sol.checkInclusion(s1, s2))
     