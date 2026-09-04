s = "a(b)s)f(b"

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for b in s:
            if b in brackets.values():
                stack.append(b)
            
            if b in brackets:
                if not stack:
                    return False
                else:
                    if brackets[b] == stack[len(stack)-1]:
                        stack.pop()
                    else:
                        return False
        
        if not stack:
            return True
        else:
            return False
            
sol = Solution()
print(sol.isValid(s))