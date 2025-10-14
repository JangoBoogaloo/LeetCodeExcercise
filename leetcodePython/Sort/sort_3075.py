from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        totalHappiness = 0
        for i in range(k):
            totalHappiness += max(happiness[i]-i, 0)
        return totalHappiness





import pytest
target = Solution()

@pytest.mark.parametrize("happiness, k, expect",
[
    ([3, 2, 1], 2, 4),
    ([1, 2, 3], 2, 4),
    ([1, 1, 1], 2, 1)
])
def test_checkType(happiness, k, expect):
    assert target.maximumHappinessSum(happiness, k) == expect