import collections
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not endWord or not beginWord or not wordList or endWord not in wordList:
            return []
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
        ans = []
        while queue: