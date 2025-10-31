class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Brute Force
        merged_list = nums1 + nums2
        merged_list.sort()

        # Mid idx
        mid = len(merged_list) // 2

        # If even
        if len(merged_list) % 2 == 0:
            return (merged_list[mid - 1] + merged_list[mid])/2
        else:
            # Odd
            return merged_list[mid]