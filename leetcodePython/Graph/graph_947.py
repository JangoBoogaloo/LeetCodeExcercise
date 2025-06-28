from typing import List
from union_find import UF

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UF()
        RANGE_LIMIT = 10001
        for row, col in stones:
            colId = col + RANGE_LIMIT
            uf.add(row), uf.add(colId)
            uf.union(row, colId)
        return len(stones) - len(uf)






import pytest
target = Solution()

@pytest.mark.parametrize("stones, expect",
[
    ([[1, 2], [1, 3]], 1),
    ([[1,2], [1,3],[2,2]], 2),
    ([[1, 2], [1, 3], [2, 2], [3, 1]], 2),
    ([[1, 2], [1, 3], [2, 2], [3, 1], [3, 4]], 3),
    ([[1, 2], [1, 3], [2, 2], [3, 1], [3, 4], [3, 2]], 5),
])
def test_removeStones(stones, expect):
    assert target.removeStones(stones) == expect