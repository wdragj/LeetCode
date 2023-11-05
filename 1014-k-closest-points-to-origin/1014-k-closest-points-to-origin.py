import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for p in points:
            x, y = p
            dist = math.sqrt((x - 0)**2 + (y - 0)**2)
            heapq.heappush(heap, (dist, p))
        
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans