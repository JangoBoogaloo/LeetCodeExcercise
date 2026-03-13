from collections import defaultdict, deque
from typing import List


class Solution:
    _MAP_CHAR = "*"

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord or not beginWord or not wordList or endWord not in wordList:
            return 0
        wordMap = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + self._MAP_CHAR + word[i+1:]
                wordMap[pattern].append(word)
        currentWords = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while currentWords:
            word, moves = currentWords.popleft()
            for i in range(len(word)):
                pattern = word[:i] + self._MAP_CHAR + word[i+1:]
                for nextWord in wordMap[pattern]:
                    if nextWord == endWord:
                        return moves + 1
                    if nextWord not in visited:
                        visited.add(nextWord)
                        currentWords.append((nextWord, moves + 1))
        return 0









