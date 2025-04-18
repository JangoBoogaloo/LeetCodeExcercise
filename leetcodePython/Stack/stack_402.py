class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stepLeft = k
        remainDigits = []
        for digit in num:
            while stepLeft and remainDigits and digit < remainDigits[-1]:
                remainDigits.pop()
                stepLeft -= 1
            remainDigits.append(digit)

        if stepLeft > 0:
            remainDigits = remainDigits[:-stepLeft]

        numStr = "".join(remainDigits).lstrip('0')
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