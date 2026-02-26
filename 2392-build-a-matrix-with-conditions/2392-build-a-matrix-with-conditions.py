from collections import defaultdict, deque
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(edges):
            indegree = [0] * (k + 1)
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                indegree[v] += 1
            order = []
            q = deque()
            for i in range(1, k + 1):
                if not indegree[i]:
                    q.append(i)
            while q:
                node = q.popleft()
                order.append(node)
                for nei in graph[node]:
                    indegree[nei] -=1
                    if not indegree[nei]:
                        q.append(nei)
            return order
        
        row_order = topo_sort(rowConditions)
        if len(row_order) != k:
            return []
        col_order = topo_sort(colConditions)
        if len(col_order) != k:
            return []
        
        matrix = [[0] * k for _ in range(k)]
        col_idx = [0] * (k + 1)
        for i in range(k):
            col_idx[col_order[i]] = i
        
        for i in range(k):
            matrix[i][col_idx[row_order[i]]] = row_order[i]
        return matrix
