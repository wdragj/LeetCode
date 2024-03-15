class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sHash, tHash = {}, {}

        for c_s, c_t in zip(s, t):
            sHash[c_s] = sHash.get(c_s, 0) + 1
            tHash[c_t] = tHash.get(c_t, 0) + 1
        
        for c in s:
            if sHash[c] != tHash.get(c, 0):
                return False
        
        return True 