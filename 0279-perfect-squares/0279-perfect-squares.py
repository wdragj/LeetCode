class Solution:
    def numSquares(self, n: int) -> int:
        q = deque()
        visited = set()

        res = 0
        q.append(0)
        while q:
            res += 1
            for _ in range(len(q)):
                cur = q.popleft()
                s = 1
                while s * s + cur <= n:
                    nxt = cur + s * s
                    if nxt == n:
                        return res
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
                    s += 1
        return res