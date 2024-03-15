class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = list(map(str, s.split(" ")))

        if len(s) != len(pattern):
            return False

        patternHash = {}
        sHash = {}

        for i in range(len(pattern)):
            if pattern[i] not in patternHash:
                patternHash[pattern[i]] = s[i]
            if s[i] not in sHash:
                sHash[s[i]] = pattern[i]

            if patternHash[pattern[i]] != s[i]:
                return False
            
        if len(sHash.keys()) != len(patternHash.keys()):
            return False
        
        return True