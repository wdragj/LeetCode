class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointers l and r
        l, r = 0, len(numbers) - 1

        while l <= r:
            sumNum = numbers[l] + numbers[r]

            # If target, return
            if sumNum == target:
                return [l + 1, r + 1]

            # If less than target increment l
            if sumNum < target:
                l += 1

            # If greater than target decrement r
            if sumNum > target:
                r -= 1