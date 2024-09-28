class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        freq = Counter(nums)
        sorted_nums = sorted(freq.keys())
        res = []
        cnt = 1

        print(sorted_nums)
        
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i+1] - sorted_nums[i] == 1:
                cnt += 1
            else:
                res.append(cnt)
                cnt = 1
        
        res.append(cnt)
        
        return max(res)