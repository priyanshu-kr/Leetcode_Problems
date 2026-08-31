from typing import List

s = "racecar"
t = "carrace"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = {}
        for n in s:
            dict_s[n] = dict_s.get(n,0)+1
            # if we don't initialise the element count with 0 here,it will return None and None+1 will give TypeError: unsupported operand type for +: 'NoneType' and 'int' 
#            print(dict_s)

        dict_t = {}
        for n in t:
            dict_t[n] = dict_t.get(n,0)+1
#        print(dict_t)

        return dict_s == dict_t

sol = Solution()
print(sol.isAnagram(s,t))

"""
Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.


Time: O(n) using get()
      O(n) if we use str.count() as it traverses the whole string for each element
Space: O(n)

s and t consist of lowercase English letters.
There are only 26 possible characters.
That means each dictionary can contain at most 26 keys, regardless of whether the string has 10 characters or 50,000 characters.

So under these specific constraints, the auxiliary space is technically: O(1)

That's an important DSA lesson:
Complexity depends not only on the code, but also on the constraints.

If the problem instead allowed arbitrary characters, and the string had n unique characters, then the dictionary could contain n keys:
"""