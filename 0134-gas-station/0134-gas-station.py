class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        start, tank = 0, 0
        for i in range(n):
            diff = gas[i] - cost[i]
            tank += diff
            if tank < 0:
                tank = 0
                start = i + 1
        return start