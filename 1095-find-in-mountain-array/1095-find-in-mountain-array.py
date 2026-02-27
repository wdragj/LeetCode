class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l, r = 0, n
        peak = -1
        while l < r:
            mid = (l + r) // 2
            mid_val = mountainArr.get(mid)
            r_val = mountainArr.get(mid + 1) if mid + 1 < n else float("-inf")
            if mid_val > r_val:
                r = mid
                peak = mid
            else:
                l = mid + 1
        if target == mountainArr.get(peak):
            return peak

        l, r = 0, peak - 1
        while l <= r:
            mid = (l + r) // 2
            mid_val = mountainArr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                l = mid + 1
            else:
                r = mid - 1
        
        l, r = n - 1, peak + 1
        while l >= r:
            mid = (l + r) // 2
            mid_val = mountainArr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                l = mid - 1
            else:
                r = mid + 1
        return -1