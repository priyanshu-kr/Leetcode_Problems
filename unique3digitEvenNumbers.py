"""
3483. Unique 3-Digit Even Numbers

You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.

Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.

 

Example 1:

Input: digits = [1,2,3,4]

Output: 12

Explanation: The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.


Example 2:

Input: digits = [0,2,2]

Output: 2

Explanation: The only 3-digit even numbers that can be formed are 202 and 220. Note that the digit 2 can be used twice because it appears twice in the array.


Example 3:

Input: digits = [6,6,6]

Output: 1

Explanation: Only 666 can be formed.


Example 4:

Input: digits = [1,3,5]

Output: 0

Explanation: No even 3-digit numbers can be formed.

 

Constraints:

3 <= digits.length <= 10
0 <= digits[i] <= 9
"""

from collections import Counter
from typing import List

digits = [1,2,2,4]
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        
        digit_freq = {}
        for n in digits:
            digit_freq[n] = digit_freq.get(n,0) + 1

        result = set()
        
        for first in range(1, 10):
            for second in range(0,10):
                for third in range(0,10,2):
                    candidate = [first, second, third]
                    candidate_freq = Counter(candidate)

                    valid = True

                    for i in candidate_freq:
                        if candidate_freq[i] > digit_freq.get(i,0):
                            valid = False
                            break
                    if valid:
                        result.add(100*first + 10*second + third)

        return len(result)

sol = Solution()
print(sol.totalNumbers(digits))