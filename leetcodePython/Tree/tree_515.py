import collections
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        level_nodes = collections.deque()
        level_nodes.append(root)
        answer = []
        while level_nodes:
            nodes_count = len(level_nodes)
            largest = float("-inf")
            for i in range(nodes_count):
                node = level_nodes.popleft()
                if node.left:
                    level_nodes.append(node.left)
                if node.right:
                    level_nodes.append(node.right)
                largest = max(largest, node.val)
            answer.append(largest)

        return answer


if __name__ == "__main__":
    sol = Solution()
    tree = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
    print(sol.largestValues(tree))
