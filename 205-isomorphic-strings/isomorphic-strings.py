class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap, tMap = {}, {}

        for i in range(len(s)):
            if s[i] not in sMap:
                sMap[s[i]] = t[i]
            if t[i] not in tMap:
                tMap[t[i]] = s[i]
            
            if sMap.get(s[i]) != t[i]:
                return False
            
        if len(sMap.keys()) != len(tMap.keys()):
            return False
        
        return True
