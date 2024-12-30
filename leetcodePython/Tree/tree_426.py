from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None

        def construct(node) -> tuple[Optional[Node], Optional[Node]]:
            if not node:
                return None, None

            leftHead, leftTail = construct(node.left)
            rightHead, rightTail = construct(node.right)
            head = node
            tail = node
            if leftHead:
                head = leftHead
                leftTail.right = node
                node.left = leftTail
            if rightHead:
                tail = rightTail
                node.right = rightHead
                rightHead.left = node
            return head, tail

        head, tail = construct(root)
        tail.right = head
        head.left = tail
        return head
