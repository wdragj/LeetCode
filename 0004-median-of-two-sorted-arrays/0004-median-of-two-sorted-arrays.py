class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        n, m = len(nums1), len(nums2)
        total = n + m
        half = total // 2

        left, right = 0, n
        while left <= right:
            i = (left + right) // 2
            j = half - i

            l1 = nums1[i - 1] if i > 0 else float('-inf')
            l2 = nums2[j - 1] if j > 0 else float('-inf')

            r1 = nums1[i] if i < n else float('inf')
            r2 = nums2[j] if j < m else float('inf')

            if l1 > r2:
                right = i - 1
            elif l2 > r1:
                left = i + 1
            else:
                if total % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return min(r1, r2)
        return 0.0