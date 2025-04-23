from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(postorder) == 0:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        post_right_root = postorder[-2]
        pre_right_root_id = preorder.index(post_right_root)
        root.left = self.constructFromPrePost(preorder[1: pre_right_root_id], postorder[:pre_right_root_id-1])
        root.right = self.constructFromPrePost(preorder[pre_right_root_id:], postorder[pre_right_root_id-1:-1])