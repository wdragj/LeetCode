class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        mid = (l + r) // 2
        nums.sort()
        return nums[mid]