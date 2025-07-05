import collections
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        if not root:
            return answer
        col_nodes = collections.defaultdict(list)
        level_nodes = collections.deque()
        level_nodes.append((root, 0))
        min_index = max_index = 0
        level = 0
        while level_nodes:
            count = len(level_nodes)
            for _ in range(count):
                current, index = level_nodes.popleft()
                min_index = min(min_index, index)
                max_index = max(max_index, index)
                col_nodes[index].append((level, current.val))
                if current.left:
                    level_nodes.append((current.left, index - 1))
                if current.right:
                    level_nodes.append((current.right, index + 1))
            level += 1

        for index in range(min_index, max_index + 1):
            col_nodes[index].sort()
            answer.append([value for level, value in col_nodes[index]])
        return answer


if __name__ == "__main__":
    solution = Solution()
    tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(3, TreeNode(5), TreeNode(7)))
    print(solution.verticalTraversal(tree))
