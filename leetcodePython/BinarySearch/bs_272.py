from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _sortInorder(self, node: Optional[TreeNode], sortedList: List[int]) -> None:
        if not node:
            return
        self._sortInorder(node.left, sortedList)
        sortedList.append(node.val)
        self._sortInorder(node.right, sortedList)

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        sortedList = []
        self._sortInorder(root, sortedList)
        left = 0
        right = len(sortedList) - k
        while left < right:
            guessStartIndex = (left + right) // 2
            guessEndIndex = guessStartIndex + k
            guessStartDistance = abs(target - sortedList[guessStartIndex])
            guessEndDistance = abs(target - sortedList[guessEndIndex])
            if guessStartDistance >= guessEndDistance:
                left = guessStartIndex + 1
            else:
                right = guessStartIndex
        return sortedList[left: left+k]
