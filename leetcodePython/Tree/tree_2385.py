import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class GraphNode:
    def __init__(self, node: TreeNode, parent=None, left=None, right=None):
        self.parent = parent
        self.node = node
        self.left = left
        self.right = right


class Solution:

    @staticmethod
    def _graph_from_start(root: Optional[TreeNode], start: int) -> Optional[TreeNode]:
        if not root:
            return None
        current = GraphNode(root)
        level_nodes = collections.deque()
        level_nodes.append(current)
        start_node = None
        while level_nodes:
            current = level_nodes.popleft()
            if current.node.val == start:
                start_node = current
            if current.node.left:
                left = GraphNode(current.node.left, current)
                current.left = left
                level_nodes.append(left)
            if current.node.right:
                right = GraphNode(current.node.right, current)
                current.right = right
                level_nodes.append(right)

        return start_node

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0
        start_node = self._graph_from_start(root, start)
        level_nodes = collections.deque()
        level_nodes.append(start_node)
        visited = set()
        minute = -1
        while level_nodes:
            node_count = len(level_nodes)
            for _ in range(node_count):
                current = level_nodes.popleft()
                visited.add(current)
                if current.left and current.left not in visited:
                    level_nodes.append(current.left)
                if current.right and current.right not in visited:
                    level_nodes.append(current.right)
                if current.parent and current.parent not in visited:
                    level_nodes.append(current.parent)
            minute += 1
        return minute
