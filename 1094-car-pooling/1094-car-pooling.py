import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        car = []
        curr_capacity = 0
        for trip in trips:
            cnt, start, end = trip
            while car and car[0][0] <= start:
                curr_capacity -= car[0][2]
                heapq.heappop(car)
            heapq.heappush(car, (end, start, cnt))
            curr_capacity += cnt
            if curr_capacity > capacity:
                return False
        return True