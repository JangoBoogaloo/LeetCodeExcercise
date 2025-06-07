from typing import List


class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        prevWinIndex, newIndex = 0, 1
        maxWin = 0
        while newIndex < len(skills):
            if skills[prevWinIndex] < skills[newIndex]:
                maxWin = 1
                prevWinIndex = newIndex
            else:
                 maxWin += 1
            if maxWin == k:
                break
            newIndex += 1
        return prevWinIndex






import pytest
target = Solution()

@pytest.mark.parametrize("skills, k, expect",
[
    ([3,2,1], 2, 0),
    ([3, 2, 1, 4], 2, 0),
    ([2, 1, 3], 2, 2),
    ([2, 1, 3], 1000, 2),
])
def test_findWinningPlayer(skills, k, expect):
    assert target.findWinningPlayer(skills, k) == expect