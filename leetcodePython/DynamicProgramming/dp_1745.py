class Solution:
    @staticmethod
    def _isPal(txt:str) -> bool:
        return txt == txt[::-1]

    def checkPartitioning(self, txt: str) -> bool:
        if len(txt) < 3:
            return False
        return self._checkPartition3(txt) or self._checkPartition3(txt[::-1])

    def _checkPartition3(self, txt: str) -> bool:
        i:int = 0
        for i in range(len(txt), 1, -1):
            if self._isPal(txt[:i]):
                i = i + 1
                break
        i -= 1
        if i == len(txt):
            return True

        if self._isPal(txt[:i]) and self._checkPartition2(txt[i:]):
            return True
        if self._isPal(txt[i:]) and self._checkPartition2(txt[:i]):
            return True
        return False

    def _checkPartition2(self, s: str) -> bool:
        for i in range(1, len(s)):
            if self._isPal(s[:i]) and self._isPal(s[i:]):
                return True
        return False