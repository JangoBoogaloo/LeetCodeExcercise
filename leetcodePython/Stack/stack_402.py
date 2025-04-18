class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        remainRemoval = k
        increaseDigits = []
        for digit in num:
            while remainRemoval and increaseDigits and digit < increaseDigits[-1]:
                increaseDigits.pop()
                remainRemoval -= 1
            increaseDigits.append(digit)

        if remainRemoval > 0:
            increaseDigits = increaseDigits[:-remainRemoval]

        numStr = "".join(increaseDigits).lstrip('0')
        return numStr if numStr else "0"


import pytest
target = Solution()

@pytest.mark.parametrize("num, k, expected",
[
    ("1234", 2, "12"),
    ("9399", 2, "39")
])
def test_removeKdigits(num, k, expected):
    assert target.removeKdigits(num, k) == expected