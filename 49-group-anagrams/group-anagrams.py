class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        uniques = {}
        anagrams = []

        for word in strs:
            sorted_word = ""
            chars = sorted([c for c in word])
            for c in chars:
                sorted_word += c    
            if sorted_word in uniques:
                uniques[sorted_word].append(word)
            else:
                uniques[sorted_word] = [word]
        return uniques.values()