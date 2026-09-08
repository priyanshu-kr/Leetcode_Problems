from typing import List

strs = ["Hello", "World", ""]

class Solution:
    
    def encode(self, strs:List[str]) -> str:
        
        encoded_string = ""
        for e in strs:
            encoded_string += str(len(e)) + '#' + e
        
        return encoded_string

    
    def decode(self, s:str) -> List[str]:

        result = []
        i = 0
  
        while i < len(s):
            
            length = ""

            while i < len(s) and s[i] != '#':

            # length = ""
            # while i < s.find("#", i):
                length += s[i]
                i += 1
                
            
            length = int(length)
            i += 1

            result.append(s[ i : i + length])

            i = i + length

        return result

sol = Solution()
encoded_string = sol.encode(strs)
print(encoded_string)
decoded_strings = sol.decode(encoded_string)
print(decoded_strings)