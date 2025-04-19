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
    ("123", "1", "23"),
    ("1231", "1", "231"),
    ("6296", "6", "629"),
    ("6926", "6", "926"),
    ("6626", "6", "662"),
    ("53565", "5", "5365"),
    ("53535", "5", "5353")
])
def test_checkType(number, digit, expect):
    assert target.removeDigit(number, digit) == expect
