import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord or not beginWord or not wordList or endWord not in wordList:
            return 0
        size = len(beginWord)
        GENERIC_CHAR = "*"
        words_combo = collections.defaultdict(list)
        for word in wordList:
            for i in range(size):
                # Replace a character to generic * so we can easily compare
                a_combo = word[:i] + GENERIC_CHAR + word[i + 1:]
                words_combo[a_combo].append(word)

        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}
        while queue:
            curr_word, level = queue.popleft()
            for i in range(size):
                word_combo = curr_word[:i] + GENERIC_CHAR + curr_word[i + 1:]
                for word in words_combo[word_combo]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                words_combo[word_combo] = []
        return 0
