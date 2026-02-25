from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        q = deque([beginWord])
        visited = set(beginWord)
        wordList = set(wordList)
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()
                if endWord == word:
                    return res
                for i in range(len(word)):
                    for letter in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + letter + word[i+1:]
                        if new_word in wordList and new_word not in visited:
                            q.append(new_word)
                            visited.add(new_word)
        return 0