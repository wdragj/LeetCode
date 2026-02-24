class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        curr_max, curr_min, res = nums[0], nums[0], nums[0]
        for i in range(1, n):
            new_max = max(nums[i], curr_max * nums[i], curr_min * nums[i])
            new_min = min(nums[i], curr_max * nums[i], curr_min * nums[i])

            curr_max = new_max
            curr_min = new_min

            res = max(res, curr_max)
        return res