class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        return ""


import pytest
target = Solution()

@pytest.mark.parametrize("number, digit, expect",
[
    ("1231", "1", "231"),
    ("9239", "9", "923"),
])
def test_checkType(number, digit, expect):
    assert target.removeDigit(number, digit) == expect