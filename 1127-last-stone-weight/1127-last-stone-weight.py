import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-val for val in stones]
        heapq.heapify(pq)
        
        while(len(pq) > 1):
            y = -heapq.heappop(pq)
            x = -heapq.heappop(pq)

            if y > x:
                heapq.heappush(pq, -(y - x))
        
        return -pq[0] if pq else 0