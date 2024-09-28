class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out_list, prefix, suffix = [0] * len(nums), [0] * len(nums), [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1
            else:
                prefix[i] = nums[i-1]*prefix[i-1]
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                suffix[-1] = 1
            else:
                suffix[i] = nums[i+1]*suffix[i+1]
        
        for i in range(len(nums)):
            out_list[i] = prefix[i]*suffix[i]
        
        return out_list