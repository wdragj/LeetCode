class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def backtrack(subset: List[int], start: int) -> None:
            ans.append(subset[:])
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(subset, i + 1)
                subset.pop()
        backtrack([], 0)
        return ans