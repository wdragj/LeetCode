class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        n = len(s)
        integer = 0
        for i, c in enumerate(s):
            # I before V and X
            if c == "I" and i+1 < n and (s[i+1] == "V" or s[i+1] == "X"):
                    integer -= 1
            # X before L and C
            elif c == "X" and i+1 < n and (s[i+1] == "L" or s[i+1] == "C"):
                    integer -= 10
            # C before D and M
            elif c == "C" and i+1 < n and (s[i+1] == "D" or s[i+1] == "M"):
                    integer -= 100
            else:
                integer += hashmap[c]
        return integer