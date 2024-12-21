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


class SolutionBottomUp:
    _countFullTreeMap = {0: [],
                         1: [TreeNode()],
                         3: [TreeNode(0, TreeNode(), TreeNode())]}

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        for count in range(3, n+1, 2):
            if count in self._countFullTreeMap:
                continue
            self._countFullTreeMap[count] = []
            for lCount in range(1, count-1, 2):
                rCount = count - lCount - 1
                for left in self._countFullTreeMap[lCount]:
                    for right in self._countFullTreeMap[rCount]:
                        root = TreeNode(0, left, right)
                        self._countFullTreeMap[count].append(root)
        return self._countFullTreeMap[n]
