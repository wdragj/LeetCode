class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap to store 
        # key: current val
        # val: current idx

        hashmap = {}

        for i, v in enumerate(nums):
            if v not in hashmap:
                hashmap[v] = i
            
            find = target - v
            if find in hashmap and hashmap[find] != i:
                return [hashmap[find], i]