class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        tot = sum(nums)

        min_sum, max_sum = nums[0], nums[0]
        curr_min, curr_max = nums[0], nums[0]
        for i in range(1, n):
            curr_max = max(nums[i], nums[i] + curr_max)
            curr_min = min(nums[i], nums[i] + curr_min)
            
            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)
        
        return max(max_sum, tot - min_sum) if max_sum > 0 else max_sum