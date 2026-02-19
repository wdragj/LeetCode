class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        c1, c2 = -1, -1
        cnt1, cnt2 = 0, 0

        for num in nums:
            if num == c1:
                cnt1 += 1
            elif num == c2:
                cnt2 += 1
            elif cnt1 == 0:
                c1 = num
                cnt1 += 1
            elif cnt2 == 0:
                c2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == c1:
                cnt1 += 1
            elif num == c2:
                cnt2 += 1
        ans = []
        if cnt1 > n // 3:
            ans.append(c1)
        if cnt2 > n // 3:
            ans.append(c2)
        return ans