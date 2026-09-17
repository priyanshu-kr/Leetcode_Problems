'''
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that
answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.


Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:
1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100
'''

from typing import List

temperatures = [73,74,75,71,69,72,76,73]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []

        # for i in range(n-1, -1, -1):
        #     while len(stack) != 0 and temperatures[i] >= stack[-1][0]:
        #         stack.pop()

        #     if len(stack) != 0:
        #         answer[i] = stack[-1][1] - i

        #     stack.append((temperatures[i], i))

        ''' we can solve this by storing only indices in the stack as we are not modifying temperature values so just access them from 'temperatures' '''

        for i in range(n-1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                answer[i] = stack[-1] - i
            
            stack.append(i)
        
        return answer

sol = Solution()
print(sol.dailyTemperatures(temperatures))