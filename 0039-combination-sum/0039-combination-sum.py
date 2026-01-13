class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        t = target
        candidates.sort()
        def backtrack(comb: List[int], start: int, t: int) -> None:
            if t == 0:
                ans.append(comb[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > t:
                    break
                comb.append(candidates[i])
                backtrack(comb, i, t - candidates[i])
                comb.pop()
        backtrack([], 0, t)
        return ans