from collections import deque
from typing import List


class Solution:
    def _findRoot(self, n: int, leftChild: List[int], rightChild: List[int]):
        children = set()
        for child in leftChild:
            children.add(child)
        for child in rightChild:
            children.add(child)
        for i in range(n):
            if i not in children:
                return i
        return -1

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        if n == 0:
            return True
        visited = set()
        queue = deque()
        root = self._findRoot(n, leftChild, rightChild)
        if root == -1:
            return False
        queue.append(root)
        while queue:
            for i in range(len(queue)):
                curr_node = queue.popleft()
                if curr_node in visited:
                    return False
                visited.add(curr_node)
                if leftChild[curr_node] != -1:
                    queue.append(leftChild[curr_node])
                if rightChild[curr_node] != -1:
                    queue.append(rightChild[curr_node])
        return len(visited) == n
