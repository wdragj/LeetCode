class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""

        for ch in s:
            if ch.isalpha() or ch.isdigit():
                ans += ch.lower()
        
        # Check if it is same back and forth
        return True if ans == ans[::-1] else False