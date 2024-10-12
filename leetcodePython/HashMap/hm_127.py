import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord or not beginWord or not wordList or endWord not in wordList:
            return 0
        size = len(beginWord)
        GENERIC_CHAR = "*"
        combination_word_map = collections.defaultdict(list)
        for word in wordList:
            for i in range(size):
                # Replace a character to generic * so we can easily compare
                a_combination = word[:i] + GENERIC_CHAR + word[i + 1:]
                combination_word_map[a_combination].append(word)

        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}
        while queue:
            curr_word, level = queue.popleft()
            for i in range(size):
                word_combination = curr_word[:i] + GENERIC_CHAR + curr_word[i + 1:]
                for word in combination_word_map[word_combination]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                combination_word_map[word_combination] = []
        return 0
