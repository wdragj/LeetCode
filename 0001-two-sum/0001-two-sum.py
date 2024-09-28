class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # left and right pointers
        l, r = 0, 1

        while l <= len(nums) -1:
            for i in range(r, len(nums)):
                if nums[l] + nums[i] == target:
                    return [l, i]
            l += 1
            r += 1
        
        return [l, r]