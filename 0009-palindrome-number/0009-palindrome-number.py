class Solution:
    def isPalindrome(self, x: int) -> bool:
        number_to_str = str(x)
        n = len(number_to_str)
        l, r = 0, n - 1

        while l < r:
            if number_to_str[l] != number_to_str[r]:
                return False
            else:
                l += 1
                r -= 1
        return True