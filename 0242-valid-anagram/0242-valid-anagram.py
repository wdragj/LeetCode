class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s, hash_t =  {}, {}
        longer = s if len(s) > len(t) else t
        for c in s:
            if c not in hash_s:
                hash_s[c] = 1
            else:
                hash_s[c] += 1
        
        for c in t:
            if c not in hash_t:
                hash_t[c] = 1
            else:
                hash_t[c] += 1
        
        for c in longer:
            if hash_s.get(c, None) != hash_t.get(c, None):
                return False
        
        return True