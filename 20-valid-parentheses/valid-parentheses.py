from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        closeP = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = deque([s[0]])
        parenthesis = deque([x for x in s[1:]])

        while(parenthesis):
            bracket = parenthesis.popleft()
            if bracket in closeP:
                if stack and closeP[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return False if stack else True