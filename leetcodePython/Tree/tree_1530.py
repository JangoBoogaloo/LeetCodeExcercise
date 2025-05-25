from typing import Optional, List
from tree import TreeNode


class Solution:
    _totalPairs: int

    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self._totalPairs = 0
        self._postOrder(root, distance)
        return self._totalPairs

    def _postOrder(self, curr: TreeNode, distance) -> List[int]:
        leafCountWithDepth = [0] * (distance + 1)
        if not curr:
            return leafCountWithDepth

        if not curr.left and not curr.right:
            leafCountWithDepth[1] = 1
            return leafCountWithDepth

        leftLeafCountWithDepth = self._postOrder(curr.left, distance)
        rightLeafCountWithDepth = self._postOrder(curr.right, distance)
        for leftLeafDepth in range(1, distance):
            for rightLeafDepth in range(1, distance):
                distanceSum = leftLeafDepth + rightLeafDepth
                if distanceSum <= distance:
                    distanceSumCombinations = leftLeafCountWithDepth[leftLeafDepth] * rightLeafCountWithDepth[rightLeafDepth]
                    self._totalPairs += distanceSumCombinations

        for depth in range(distance, 0, -1):
            leafCountWithDepth[depth] = leftLeafCountWithDepth[depth - 1] + rightLeafCountWithDepth[depth - 1]
        return leafCountWithDepth
