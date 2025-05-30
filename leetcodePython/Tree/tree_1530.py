from typing import Optional, List
from tree import TreeNode


class Solution:
    _totalPairs: int

    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self._totalPairs = 0
        self._postOrder(root, distance)
        return self._totalPairs

    def _postOrder(self, curr: TreeNode, distance) -> List[int]:
        leafCountToParentWithDistance = [0] * (distance + 1)
        if not curr:
            return leafCountToParentWithDistance

        if not curr.left and not curr.right:
            leafCountToParentWithDistance[1] = 1
            return leafCountToParentWithDistance

        leftLeafCountToCurrentWithDistance = self._postOrder(curr.left, distance)
        rightLeafCountToCurrentWithDistance = self._postOrder(curr.right, distance)
        for leftLeafDepth in range(1, distance):
            for rightLeafDepth in range(1, distance):
                distanceSum = leftLeafDepth + rightLeafDepth
                if distanceSum <= distance:
                    distanceSumCombinations = leftLeafCountToCurrentWithDistance[leftLeafDepth] * rightLeafCountToCurrentWithDistance[rightLeafDepth]
                    self._totalPairs += distanceSumCombinations

        for depth in range(distance, 0, -1):
            leafCountToParentWithDistance[depth] = leftLeafCountToCurrentWithDistance[depth - 1] + rightLeafCountToCurrentWithDistance[depth - 1]
        return leafCountToParentWithDistance






import pytest

target = Solution()

@pytest.mark.parametrize("nums, distance, expect",
[
    ([1, 2, 3, None, 4], 3, 1),
    ([1, 2, 3, 4, 5, 6, 7], 3, 2),
    ([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2], 3, 1)
])
def test_countPairs(nums, distance, expect):
    tree = TreeNode.deserialize(nums)
    assert target.countPairs(tree, distance) == expect
