import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        k = len(points)
        adj = { i:[] for i in range(k) }
        for i in range(k):
            x1, y1 = points[i]
            for j in range(i + 1, k):
                x2, y2 = points[j]
                val = abs(x1-x2) + abs(y1-y2)
                adj[i].append([val, j])
                adj[j].append([val, i])
        
        res = 0
        visited, pq = set(), [[0, 0]]
        while len(visited) < k:
            dist, point = heapq.heappop(pq)
            if point in visited:
                continue
            res += dist
            visited.add(point)
            for neighbor in adj[point]:
                val, nei = neighbor
                heapq.heappush(pq, [val, nei])
        
        return res