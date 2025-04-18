class Solution:
    def checkType(self, text, integer, dictionary) -> bool:
        return isinstance(text, str) and isinstance(integer, int) and isinstance(dictionary, dict)


import pytest
target = Solution()

@pytest.mark.parametrize("text, integer, dictionary, expect",
[
    ("1", 2, {1:1, 2:2}, True),
    ("1", 2, [], False),

])
def test_checkType(text, integer, dictionary, expect):
    assert target.checkType(text, integer, dictionary) == expect