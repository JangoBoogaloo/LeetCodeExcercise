from typing import List


class Solution:
    @staticmethod
    def _putRepeatCount(repeatCount: int, resultIndex: int, chars:List[str]) -> int:
        repeatCountStr = str(repeatCount)
        for ch in repeatCountStr:
            chars[resultIndex] = ch
            resultIndex += 1
        return resultIndex

    def compress(self, chars: List[str]) -> int:
        repeatCh = ''
        repeatCount = 1
        resultIndex = 0
        for i in range(len(chars)):
            if chars[i] == repeatCh:
                repeatCount += 1
                continue
            if repeatCount > 1:
                resultIndex = self._putRepeatCount(repeatCount, resultIndex, chars)
                repeatCount = 1
            repeatCh = chars[i]
            chars[resultIndex] = repeatCh
            resultIndex += 1
        if repeatCount > 1:
            resultIndex = self._putRepeatCount(repeatCount, resultIndex, chars)
        return resultIndex







