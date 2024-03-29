class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        # the next becomes the child of the curr
        curr = self.trie
        # add character one by one
        for char in word:
            # move curr to deeper trie along the word
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        # when reaching end, marks it isWord
        curr['#'] = True    

    def search(self, word: str) -> bool:
        # uses index to move across recursion 
        # identify dot to special path
        # return boolean from bottom to starting        
        return self.match(self.trie, word, 0)
    
    def match(self, node, word, index):
        # base
        if index == len(word): 
            return '#' in node
        
        if word[index]=='.':
            for child in node:
                # dfs - move to next recursion by incrementinf index 1
                if child!='#' and self.match(node[child], word, index+1):
                    return True 
            return False # no find in every path
            
        if word[index] not in node: 
            return False        
        return self.match(node[word[index]], word, index+1) 


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)