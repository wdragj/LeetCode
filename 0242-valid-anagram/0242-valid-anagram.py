from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = defaultdict(int)
        freq_t = defaultdict(int)

        for c in s:
            freq_s[c] += 1
        for c in t:
            freq_t[c] += 1

        return True if freq_s.items() == freq_t.items() else False