"""
3870. Count Commas in Range
3871. Count Commas in Range II

You are given an integer n.

Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.

In standard formatting:

A comma is inserted after every three digits from the right.
Numbers with fewer than 4 digits contain no commas.
 

Example 1:

Input: n = 1002

Output: 3

Explanation:

The numbers "1,000", "1,001", and "1,002" each contain one comma, giving a total of 3.

Example 2:

Input: n = 998

Output: 0

Explanation:

All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.

 

Constraints:

1 <= n <= 10^5
"""

n = 123456

class Solution:
    def countCommas(self, n: int) -> int:

        total_commas = 0

        # for d in range(4, len(str(n))+1):
        #     start = 10**(d-1)
        #     end = min(n, 10**d - 1 )
        #     count = end - start + 1
        #     commas_per_number = (d-1)//3
        #     total_commas += count * commas_per_number
        
        T = 10**3
        while T<=n:
            total_commas += n-T+1
            T *= 10**3
    
        return total_commas

sol = Solution()
print(sol.countCommas(n))