from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = defaultdict(int)
        most_freq = 0
        ans = 0
        left = right = 0
        while right < len(s):
            hash_map[s[right]] += 1
            most_freq = max(most_freq, hash_map[s[right]])
            if (right - left + 1) > most_freq + k:
                hash_map[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans