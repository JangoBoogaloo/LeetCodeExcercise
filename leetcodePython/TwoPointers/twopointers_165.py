class Solution:
    def _nextVersion(self, txt:str, startIndex) -> tuple[int, int]:
        version = 0
        if startIndex > len(txt) - 1:
            return version, startIndex
        endIndex = startIndex
        while endIndex < len(txt) and txt[endIndex] != ".":
            endIndex += 1
        if endIndex != len(txt) - 1:
            version = int(txt[startIndex:endIndex])
        else:
            version = int(txt[startIndex:])
        nextStart = endIndex + 1
        return version, nextStart

    def compareVersion(self, version1: str, version2: str) -> int:
        i1, i2 = 0, 0
        while i1 < len(version1) or i2 < len(version2):
            v1, i1 = self._nextVersion(version1,i1)
            v2, i2 = self._nextVersion(version2,i2)
            if v1 != v2:
                return 1 if v1 > v2 else -1
        return 0






