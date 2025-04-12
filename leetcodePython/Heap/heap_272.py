from typing import List, Optional
from heapq import heappush, heappop

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        distanceMaxHeap = []
        self._dfs(root, distanceMaxHeap, target, k)
        return [value for _, value in distanceMaxHeap]

    def _dfs(self, current: Optional[TreeNode], distanceMaxHeap: List[tuple[float, float]], target: float, kLimit: int) -> None:
        if not current:
            return
        currentDistance = abs(current.val - target)
        heappush(distanceMaxHeap, (-currentDistance, current.val))
        if len(distanceMaxHeap) > kLimit:
            heappop(distanceMaxHeap)
        self._dfs(current.left, distanceMaxHeap, target, kLimit)
        self._dfs(current.right, distanceMaxHeap, target, kLimit)

