from typing import List, Deque, Set, Dict
from collections import deque

class Solution:
    def __init__(self):
        self.neighbours_reversed: Dict[str, List[str]] = {}
        self.currPath: List[str] = []
        self.shortestPaths: List[List[str]] = []

    def findNeighbors(self, word: str, wordSet: Set[str]) -> List[str]:
        neighbors: List[str] = []
        charList = list(word)
        for i in range(len(charList)):
            oldChar = charList[i]
            # replace the i-th character with all letters from a to z except the original character
            for c in "abcdefghijklmnopqrstuvwxyz":
                # skip if the replaced character is same as existing character
                if c == oldChar:
                    continue
                charList[i] = c
                newWord = "".join(charList)
                # skip if the word is not present in the wordSet
                if newWord not in wordSet:
                    continue
                neighbors.append(newWord)
            charList[i] = oldChar
        return neighbors

    def backtrack(self, source: str, destination: str):
        # store the path if we reached the endWord
        if source == destination:
            tempPath = self.currPath.copy()
            tempPath.reverse()
            self.shortestPaths.append(tempPath)

        if source not in self.neighbours_reversed:
            return

        for neighbor in self.neighbours_reversed[source]:
            self.currPath.append(neighbor)
            self.backtrack(neighbor, destination)
            self.currPath.pop()

    def bfs(self, beginWord: str, wordSet: Set[str]):
        queue: Deque[str] = deque([beginWord])
        # remove the root word which is the first layer in the BFS
        wordSet.discard(beginWord)  # discard does nothing if element is not found
        isEnqueued: Dict[str, bool] = {beginWord: True}
        while queue:
            # visited will store the words of current layer
            visited: List[str] = []
            for _ in range(len(queue)):
                currWord = queue.popleft()
                # findNeighbors will have the adjacent words of the currWord
                neighbors = self.findNeighbors(currWord, wordSet)
                for neighbor in neighbors:
                    visited.append(neighbor)
                    if neighbor not in self.neighbours_reversed:
                        self.neighbours_reversed[neighbor] = []
                    # add the edge from neighbor to currWord in the list
                    self.neighbours_reversed[neighbor].append(currWord)
                    if neighbor not in isEnqueued:
                        queue.append(neighbor)
                        isEnqueued[neighbor] = True
            # removing the words of the previous layer
            for word in visited:
                wordSet.discard(word)

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)

        self.bfs(beginWord, wordSet)

        # reverse start from end word
        self.currPath = [endWord]
        self.backtrack(endWord, beginWord)

        return self.shortestPaths
