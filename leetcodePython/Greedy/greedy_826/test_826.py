from greedy_826_sort_profit import Solution

import pytest
sol = Solution()

@pytest.mark.parametrize("difficulties, profits, workers, expect",
[
    ([1, 2, 3], [10, 20, 30], [1, 2, 3], 60),
    ([1, 3, 2], [10, 30, 20], [1, 3, 2], 60),
    ([1, 2, 3], [30, 20, 10], [1, 2, 3], 90),
    ([4, 5, 6], [10, 20, 30], [1, 2, 3], 0),
])
def test_checkType(difficulties, profits, workers, expect):
    assert sol.maxProfitAssignment(difficulties, profits, workers) == expect