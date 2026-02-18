class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": "+"
        }

        def backtrack(comb, start):
            if not digits:
                return
            if len(comb) == len(digits):
                ans.append("".join(comb))
                return
            for i in range(start, len(digits)):
                if i > start:
                    continue
                for letter in keypad[digits[i]]:
                    comb.append(letter)
                    backtrack(comb, start + 1)
                    comb.pop()
        
        ans = []
        backtrack([], 0)
        return ans