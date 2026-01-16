import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(enq_time, process_time, i) for i, (enq_time, process_time) in enumerate(tasks)]
        tasks.sort(key = lambda x: x[0])
        n = len(tasks)
        i = 0
        curr_time = 0
        min_heap = []
        ans = []
        while i < n or min_heap:
            while i < n and tasks[i][0] <= curr_time:
                enqueueTime, processingTime, task_i = tasks[i]
                heapq.heappush(min_heap, (processingTime, task_i))
                i += 1
            
            if min_heap:
                processingTime, task_i = heapq.heappop(min_heap)
                ans.append(task_i)
                curr_time += processingTime
            else:
                curr_time = tasks[i][0]
        return ans
