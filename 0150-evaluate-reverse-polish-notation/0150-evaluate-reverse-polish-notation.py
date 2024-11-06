from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        stackTokens = deque(tokens)

        while stackTokens:
            item = stackTokens.popleft()

            if item == '+':
                stack.append(stack.pop() + stack.pop())
            elif item == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif item == '*':
                stack.append(stack.pop() * stack.pop())
            elif item == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(item))

        return stack[0]