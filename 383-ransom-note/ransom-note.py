class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashDict = {}
        for c in magazine:
            if c not in hashDict:
                hashDict[c] = 1
            else:
                hashDict[c] += 1

        for c in ransomNote:
            if c not in hashDict:
                return False
            else:
                if hashDict.get(c) == 0:
                    return False
                else:
                    hashDict[c] -= 1
        
        return True