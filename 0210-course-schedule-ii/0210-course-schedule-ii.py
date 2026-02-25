from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for v, u in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        ans = []
        q = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            ans.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return ans if sum(indegree) == 0 else []