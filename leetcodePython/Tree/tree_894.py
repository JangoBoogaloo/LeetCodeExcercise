from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    _countFullTreeMap = {0: [],
                         1: [TreeNode()],
                         3: [TreeNode(0, TreeNode(), TreeNode())]}

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        def backtrack(nodeCount: int) -> List[Optional[TreeNode]]:
            if nodeCount in self._countFullTreeMap:
                return self._countFullTreeMap[nodeCount]
            trees = []
            for i in range(1, nodeCount, 2):
                leftTrees = backtrack(i)
                rightTrees = backtrack(nodeCount - i - 1)

                for left in leftTrees:
                    for right in rightTrees:
                        root = TreeNode(0, left, right)
                        trees.append(root)
            self._countFullTreeMap[nodeCount] = trees
            return self._countFullTreeMap[nodeCount]

        backtrack(n)
        return self._countFullTreeMap[n]
