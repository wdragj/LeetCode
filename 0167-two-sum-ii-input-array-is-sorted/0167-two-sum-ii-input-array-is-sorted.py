class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l <= r:
            sumNum = numbers[l] + numbers[r]

            # Equals target
            if sumNum == target:
                return [l + 1, r + 1]
            
            # Less than target
            if sumNum < target:
                l += 1
            
            # Greater than target
            if sumNum > target:
                r -= 1
            