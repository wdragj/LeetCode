class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        behind, ahead = 0, 0
        char_count = defaultdict(int)
        char_count[s[ahead]] += 1
        max_length = 0

        while ahead < len(s):
            length = ahead - behind + 1
            max_freq = max(char_count.values())
            if length - max_freq <= k:
                max_length = max(length, max_length)
                ahead += 1
                if ahead == len(s):
                    break
                char_count[s[ahead]] += 1
            else:
                char_count[s[behind]] -= 1
                behind += 1

        return max_length