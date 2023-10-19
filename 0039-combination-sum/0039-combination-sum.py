from collections import deque

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        queue = deque() # [cur_target, cur_ans, cand_idx]
        queue.append((target, [], 0))
        ans = []
        while queue:
            cur_target, cur_ans, cand_idx = queue.popleft()
            for i in range(cand_idx, len(candidates)):
                new_target = cur_target - candidates[i]
                if new_target == 0:
                    ans.append(cur_ans + [candidates[i]])
                elif new_target > 0:
                    queue.append((cur_target - candidates[i], cur_ans + [candidates[i]], i))
        return ans