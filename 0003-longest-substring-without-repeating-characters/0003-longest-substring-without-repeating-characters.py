class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        ans = 0
        left = right = 0
        while right < len(s):
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
            unique.add(s[right])
            ans = max(ans, right - left + 1)
            right += 1
        return ans