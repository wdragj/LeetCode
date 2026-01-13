from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        leaves = [i for i in range(n) if indegree[i] == 1]
        remaining = n

        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []

            for node in leaves:
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 1:
                        new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves