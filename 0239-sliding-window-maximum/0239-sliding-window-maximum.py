from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)
        dq = deque([])
        left = right = 0
        while right < n:
            while dq and dq[-1][0] < nums[right]:
                dq.pop()
            dq.append((nums[right], right))
            if right - left + 1 == k:
                if left > dq[0][1]:
                    dq.popleft()
                ans.append(dq[0][0])
                left += 1
            right += 1
        return ans