from collections import defaultdict
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = defaultdict(int)
        curr_meetings = []
        avail = list(range(n))
        heapq.heapify(avail)
        meetings.sort(key=lambda x: x[0])

        for start, end in meetings:
            while curr_meetings and curr_meetings[0][0] <= start:
                end_time, room_num = heapq.heappop(curr_meetings)
                heapq.heappush(avail, room_num)
            if avail:
                room_num = heapq.heappop(avail)
                heapq.heappush(curr_meetings, (end, room_num))
            else:
                end_time, room_num = heapq.heappop(curr_meetings)
                heapq.heappush(curr_meetings, (end_time + (end - start), room_num))
            rooms[room_num] += 1

        return max(range(n), key=lambda i: rooms[i])