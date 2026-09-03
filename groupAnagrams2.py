# groups = {}

# for each string:
#     create [0] * 26
#     count every character using its alphabet index
#     convert freq list → tuple
#     if tuple exists:
#         append string
#     else:
#         create a new group

# return groups.values()



strs = ["act", "pots", "tops", "cat", "stop", "pit"]

class Solution:
    def groupAnagrams2(self, strs):
        
        groups = {}

        for each_str in strs:
            
            freq = [0]*26           # created fixed-length list bcz problem constraints are lowercase letters only i.e. 26

            for char in each_str:
                index = ord(char) - ord('a')
                freq[index] += 1
            
# ord() gives the Unicode code point of a character.

# Because lowercase letters are consecutive:

# ord('a') → starting position
# ord('b') → starting position + 1
# ord('c') → starting position + 2
# ...

# Therefore:

# ord('c') - ord('a')  # 2

# So for "cat":

# 'c' → index 2 → freq[2] += 1
# 'a' → index 0 → freq[0] += 1
# 't' → index 19 → freq[19] += 1

# giving a frequency representation equivalent to:

# a:1, b:0, c:1, ..., t:1, ..., z:0

            signature = tuple(freq)

            if signature in groups:
                groups[signature].append(each_str)
            else:
                groups[signature] = [each_str]

        return list(groups.values())
    
sol = Solution()
print(sol.groupAnagrams2(strs))


# Time: O(n · k) where n is no. of strings in list and k is length of each str
# Space: O(n · k) including the output; auxiliary space is effectively O(1) for the fixed 26-character alphabet.