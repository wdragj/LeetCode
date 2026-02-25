class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(comb: List[int], start: int) -> None:
            if len(comb) == k:
                ans.append(comb[:])
                return
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(comb, i + 1)
                comb.pop()
        backtrack([], 1)
        return ans