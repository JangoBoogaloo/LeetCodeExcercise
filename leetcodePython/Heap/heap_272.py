import bisect
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionSort:
    def _dfs(self, node: Optional[TreeNode], tree_values: List[int]) -> None:
        if not node:
            return
        tree_values.append(node.val)
        self._dfs(node.left, tree_values)
        self._dfs(node.right, tree_values)

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        tree_values = []
        self._dfs(root, tree_values)
        tree_values.sort(key=lambda x: (abs(x - target), x))
        return tree_values[:k]


from heapq import heappush, heappop


class SolutionHeap:
    def _dfs(self, node: Optional[TreeNode], heap: List[int], target: float, k: int) -> None:
        if not node:
            return
        if len(heap) < k:
            heappush(heap, (-abs(node.val - target), node.val))
        else:
            new_diff = abs(node.val - target)
            if new_diff < abs(heap[0][0]):
                heappop(heap)
                heappush(heap, (-new_diff, node.val))
        self._dfs(node.left, heap, target, k)
        self._dfs(node.right, heap, target, k)

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        heap = []
        self._dfs(root, heap, target, k)
        return [x[1] for x in heap]


class SolutionTwoPointers:
    def _inorder(self, node: Optional[TreeNode], tree_values: List[int]) -> None:
        if not node:
            return
        self._inorder(node.left, tree_values)
        tree_values.append(node.val)
        self._inorder(node.right, tree_values)

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        tree_values = []
        self._inorder(root, tree_values)

        left = bisect.bisect_left(tree_values, target) - 1
        right = left + 1
        ans = []
        while len(ans) < k:
            if right == len(tree_values):
                ans.append(tree_values[left])
                left -= 1
            elif abs(tree_values[left] - target) <= abs(tree_values[right] - target):
                ans.append(tree_values[left])
                left -= 1
            else:
                ans.append(tree_values[right])
                right += 1
        return ans

class SolutionBinarySearch:
    def _inorder(self, node: Optional[TreeNode], tree_values: List[int]) -> None:
        if not node:
            return
        self._inorder(node.left, tree_values)
        tree_values.append(node.val)
        self._inorder(node.right, tree_values)

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        tree_values = []
        self._inorder(root, tree_values)
        left = 0
        right = len(tree_values) - k
        while left < right:
            mid = (left + right) // 2
            if abs(target - tree_values[mid]) >= abs(target - tree_values[mid + k]):
                left = mid + 1
            else:
                right = mid
        return tree_values[left: left + k]