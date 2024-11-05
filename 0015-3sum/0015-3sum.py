class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # Sort the nums
        nums.sort()
        
        # Choose a target num (pivot)
        for i, target in enumerate(nums):
            if i > 0 and target == nums[i - 1]:
                continue
            
            # Two pointers l and r
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = target + nums[l] + nums[r]
                
                # ThreeSum is greater than 0
                if threeSum > 0:
                    r -= 1

                # ThreeSum is less than 0
                elif threeSum < 0:
                    l += 1

                # ThreeSum is 0
                else:
                    ans.append([target, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return ans