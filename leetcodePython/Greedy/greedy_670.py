class Solution:
    def maximumSwap(self, num: int) -> int:
        numStr = list(str(num))
        if len(numStr) < 2:
            return num

        maxDigitIndex = len(numStr)-1
        leftMostSmallNumIndex, rightMostBigIndex = -1, -1
        for i in range(len(numStr)-2, -1, -1):
            if numStr[i] > numStr[maxDigitIndex]:
                maxDigitIndex = i
            elif numStr[i] < numStr[maxDigitIndex]:
                leftMostSmallNumIndex = i
                rightMostBigIndex = maxDigitIndex
        if leftMostSmallNumIndex != -1:
            numStr[leftMostSmallNumIndex], numStr[rightMostBigIndex] = numStr[rightMostBigIndex], numStr[leftMostSmallNumIndex]
        return int("".join(numStr))


import pytest
target = Solution()

@pytest.mark.parametrize("num,expect",
[
    (123, 321),
    (1991, 9911),
])
def test_checkType(num,expect):
    assert target.maximumSwap(num) == expect
