class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        digits = list(number)
        digitIndex = -1
        for i in range(len(digits)):
            if digits[i] == digit:
                digitIndex = i
                if digitIndex < len(digits) - 1 and digits[digitIndex] < digits[digitIndex + 1]:
                    break
        digits[digitIndex] = ""
        return "".join(digits)


import pytest
target = Solution()

@pytest.mark.parametrize("number, digit, expect",
[
    ("557", "5", "57"),
    ("56565", "5", "6565"),
    ("54565", "5", "5465"),
    ("54545", "5", "5454")
])
def test_checkType(number, digit, expect):
    assert target.removeDigit(number, digit) == expect
