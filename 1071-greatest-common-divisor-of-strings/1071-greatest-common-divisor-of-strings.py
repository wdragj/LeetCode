from collections import Counter
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        m, n = len(str1), len(str2)
        if n > m:
            m, n = n, m
            str1, str2 = str2, str1

        ans_len = math.gcd(n, m)
        return str2[:ans_len]