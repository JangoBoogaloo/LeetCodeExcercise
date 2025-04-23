from enum import Enum
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class NodeType (Enum):
    Root = 0
    LeftBound = 1
    RightBound = 2
    Other = 3

class Solution:
    def _leftChildType(self, node: TreeNode, nodeType: NodeType) -> NodeType:
        match nodeType:
            case NodeType.LeftBound | NodeType.Root:
                return NodeType.LeftBound
            case NodeType.RightBound if not node.right:
                return NodeType.RightBound
            case _:
                return NodeType.Other

    def _rightChildType(self, node: TreeNode, nodeType: NodeType) -> NodeType:
        match nodeType:
            case NodeType.RightBound | NodeType.Root:
                return NodeType.RightBound
            case NodeType.LeftBound if not node.left:
                return NodeType.LeftBound
            case _:
                return NodeType.Other

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        leftBound = []
        leaves = []
        rightBound = deque()

        def preorder(node: Optional[TreeNode], nodeType: NodeType) -> None:
            if not node:
                return
            match nodeType:
                case NodeType.Root | NodeType.LeftBound:
                    leftBound.append(node.val)
                case NodeType.RightBound:
                    rightBound.appendleft(node.val)
                case NodeType.Other if not node.left and not node.right:
                    leaves.append(node.val)

            leftChildType = self._leftChildType(node, nodeType)
            preorder(node.left, leftChildType)
            rightChildType = self._rightChildType(node, nodeType)
            preorder(node.right, rightChildType)

        preorder(root, NodeType.Root)
        return leftBound + leaves + list(rightBound)