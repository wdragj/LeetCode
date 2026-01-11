from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map_t = Counter(t)
        count = len(t)

        left = right = 0
        min_len = float('inf')

        while right < len(s):
            if map_t[s[right]] > 0:
                count -= 1
            map_t[s[right]] -= 1

            while count == 0:
                if right - left + 1 < min_len:
                    start = left
                    min_len = right - left + 1
                if map_t[s[left]] == 0:
                    count += 1
                map_t[s[left]] += 1
                left += 1

            right += 1
        return s[start:start + min_len] if min_len != float('inf') else ''