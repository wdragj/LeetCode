class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        l, r = 0, 0
        while l < len(word1) and r < len(word2):
            res.append(word1[l])
            res.append(word2[r])
            l += 1
            r += 1
        
        if l < len(word1):
            return "".join(res + [word1[l:]])
        elif r < len(word2):
            return "".join(res + [word2[r:]])
        else:
            return "".join(res)