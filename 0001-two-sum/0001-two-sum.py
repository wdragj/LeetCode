class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # a + b = target
        # a = target - b
        l, r = 0, len(nums)
        hashmap = {}

        for i, v in enumerate(nums):
            if v in hashmap:
                return [i, hashmap[v]]

            a = target - v
            if a not in hashmap:
                hashmap[a] = i
