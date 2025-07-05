from typing import List, Optional


class Trie:
    def __init__(self):
        self._nextCharMap = {}
        self._TERMINATE = "*"

    def insert(self, word: str) -> None:
        currentMap = self._nextCharMap
        for ch in word:
            if ch not in currentMap:
                currentMap[ch] = {}
            currentMap = currentMap[ch]
        currentMap[self._TERMINATE] = {}

    def search(self, word: str) -> bool:
        currentMap = self._nextCharMap
        for ch in word:
            if ch not in currentMap:
                return False
            currentMap = currentMap[ch]
        return self._TERMINATE in currentMap

    def startsWith(self, prefix: str) -> bool:
        currentMap = self._nextCharMap
        for ch in prefix:
            if ch not in currentMap:
                return False
            currentMap = currentMap[ch]
        return True

    def _getMapOfPrefix(self, prefix: str) -> Optional[dict]:
        currentMap = self._nextCharMap
        for ch in prefix:
            if ch not in currentMap:
                return None
            currentMap = currentMap[ch]
        return currentMap

    def wordsWithPrefix(self, prefix: str) -> List[str]:
        words = []
        currentMap = self._getMapOfPrefix(prefix)
        if not currentMap:
            return words

        def dfs(nextMap, current: List[str]):
            if self._TERMINATE in nextMap:
                words.append("".join(current))
                if len(nextMap) == 1:
                    return
            for ch in nextMap:
                current.append(ch)
                dfs(nextMap[ch], current)
                current.pop()
        dfs(currentMap, [prefix])
        return words
