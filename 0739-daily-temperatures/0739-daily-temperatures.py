from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = deque()

        for i, v in enumerate(temperatures):
            # Base case: stack is empty first goes in
            if i == 0:
                stack.append((i, v))
            
            # Greater than top of stack, find difference
            while stack and stack[-1][1] < v:
                top = stack.pop()
                idx, val = top
                ans[idx] = i - idx
            
            # Less than top of stack, to stack
            stack.append((i, v))
        
        return ans