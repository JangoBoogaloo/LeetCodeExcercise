class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:


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