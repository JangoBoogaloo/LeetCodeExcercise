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