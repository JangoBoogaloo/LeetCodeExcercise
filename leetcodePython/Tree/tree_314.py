import collections
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        col_node_map = collections.defaultdict(list)

        nodes = collections.deque()
        nodes.append((root, 0))
        min_index = max_index = 0
        while len(nodes) > 0:
            node, index = nodes.popleft()
            min_index = min(min_index, index)
            max_index = max(max_index, index)
            col_node_map[index].append(node.val)
            if node.left:
                nodes.append((node.left, index - 1))
            if node.right:
                nodes.append((node.right, index + 1))
        return [col_node_map[key] for key in range(min_index, max_index + 1)]


if __name__ == "__main__":
    sol = Solution()
    tree = TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0)), TreeNode(8, TreeNode(1), TreeNode(7)))
    ans = sol.verticalOrder(tree)
    print(ans)
