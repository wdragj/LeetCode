class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def isPali(l, r) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        def backtrack(substring: List[int], start: int) -> None:
            if start >= len(s):
                ans.append(substring[:])
                return
            for i in range(start, len(s)):
                if isPali(start, i):
                    substring.append(s[start:i+1])
                    backtrack(substring, i + 1)
                    substring.pop()
        backtrack([], 0)
        return ans