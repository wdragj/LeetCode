from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = right = 0
        s1_dict = Counter(s1)
        curr_dict = defaultdict(int)
        window_size = len(s1)

        while right < len(s2):
            curr_dict[s2[right]] += 1

            if right - left + 1 == window_size:
                if s1_dict == curr_dict:
                    return True
                curr_dict[s2[left]] -= 1
                if curr_dict[s2[left]] == 0:
                    del curr_dict[s2[left]]
                left += 1
            right += 1
        
        return False