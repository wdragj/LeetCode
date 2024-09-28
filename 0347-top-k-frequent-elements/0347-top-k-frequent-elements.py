import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        res = []

        for num in nums:
            hashmap[num] += 1
        
        heap = []
        for key, v in hashmap.items():
            heapq.heappush(heap, (-v, key))
        
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res