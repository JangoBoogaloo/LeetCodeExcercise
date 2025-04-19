class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        biggerDigitIndex = 0
        smallerExist = False
        i = 0
        for i in range(1, len(digits)):
            if digits[i-1] < digits[i]:
                biggerDigitIndex = i
            elif digits[i-1] == digits[i]:
                continue
            else:
                smallerExist = True
                break
        if not smallerExist:
            return n
        digits[biggerDigitIndex] = str(int(digits[biggerDigitIndex]) - 1)
        remain9 = ["9"]*(len(digits)-1-biggerDigitIndex)
        digits = digits[:biggerDigitIndex+1] + remain9
        numStr = "".join(digits).lstrip("0")
        return int(numStr)


import pytest
target = Solution()

@pytest.mark.parametrize("n, expect",
[
    (10, 9),
    (333, 333),
    (332, 299),
    (343, 339),
    (2332, 2299)
])
def test_monotoneIncreasingDigits(n, expect):
    assert target.monotoneIncreasingDigits(n) == expect
