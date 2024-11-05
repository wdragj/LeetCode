from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # Open brackets must be closed by same type
        # Open brackets must be closed in the correct order
        # Every close bracket has a corresponding open bracket of same type

        openB = {
            '(',
            '{',
            '['
        }

        closeB = {
            ')',
            '}',
            ']'
        }

        stack = deque()
        stack.append(s[0])

        for c in s[1:]:
            # If c is a opening bracket add it to the stack
            if c in openB:
                stack.append(c)
            # If c is a closing bracket check the top of the stack
            else:
                if stack:
                    if c == ')' and stack[-1] == '(':
                        stack.pop()
                    elif c == '}' and stack[-1] == '{':
                        stack.pop()
                    elif c == ']' and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        return True if not stack else False