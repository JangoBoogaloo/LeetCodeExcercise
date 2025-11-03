from typing import List


class Solution:
    def _waysStartAt(self, charIndex:int, waysStartAt: List[int], txt: str) -> int:
        if charIndex == len(txt):
            return 1
        if txt[charIndex] == "0":
            return 0
        if charIndex == len(txt) - 1:
            return 1
        if waysStartAt[charIndex]:
            return waysStartAt[charIndex]
        ways = self._waysStartAt(charIndex + 1, waysStartAt, txt)

        if 10 <= int(txt[charIndex:charIndex+2]) <= 26:
            ways += self._waysStartAt(charIndex + 2, waysStartAt, txt)
        waysStartAt[charIndex] = ways
        return waysStartAt[charIndex]

    def numDecodings(self, s: str) -> int:
        waysStartAt = [0] * len(s)
        return self._waysStartAt(0, waysStartAt, s)






