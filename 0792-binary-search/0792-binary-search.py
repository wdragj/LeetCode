class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            # If target exists, return its index
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l += 1
            elif nums[mid] > target:
                r -= 1
        
        # Otherwise, return -1
        return -1