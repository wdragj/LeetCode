class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(perm: List[int], used: set, visited: set) -> None:
            if len(perm) == n:
                if tuple(perm) not in visited:
                    ans.append(perm[:])
                    visited.add(tuple(perm[:]))
                    return
            
            for i in range(n):
                if i in used:
                    continue
                else:
                    perm.append(nums[i])
                    used.add(i)
                    backtrack(perm, used, visited)
                    perm.pop()
                    used.remove(i)

        
        backtrack([], set(), set())
        return ans