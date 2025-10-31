class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If no common prefix, return empty string ""
        # Trie

        root = TrieNode()

        for word in strs:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr.count += 1
                curr = curr.children[c]
        
        ans = ""
        curr = root

        while len(curr.children) == 1 and curr.count == len(strs):
            ans += list(curr.children.keys())[0]
            curr = curr.children[list(curr.children.keys())[0]]
        
        return ans