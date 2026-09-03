from typing import List

nums = [1,1,2,3,3,4,4,4,5]

k = 2

class Solution:
    def topKfrequentElements(self, nums:List[int], k:int):
        
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        # print(freq)
        
        freq_buckets = {}
        for element, count in freq.items():
            if count not in freq_buckets:
                freq_buckets[count] = []
            
            freq_buckets[count].append(element)
        
        # print(freq_buckets)

        result = []
        for freq in range(len(nums), 0, -1):
            if freq in freq_buckets:
                # print(freq)
                for element in freq_buckets[freq]:

                    result.append(element)

                    if len(result) == k:
                        return result

sol = Solution()
print(sol.topKfrequentElements(nums, k))