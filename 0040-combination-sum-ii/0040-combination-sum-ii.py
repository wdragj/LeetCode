class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        used = set()
        def backtrack(comb: List[int], start: int, t: int) -> None:
            if t == 0:
                if tuple(comb[:]) not in used:
                    ans.append(comb[:])
                    used.add(tuple(comb[:]))
                    return
            
            for i in range(start, len(candidates)):
                if candidates[i] > t:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                comb.append(candidates[i])
                backtrack(comb, i + 1, t - candidates[i])
                comb.pop()
        
        backtrack([], 0, t = target)
        return ans