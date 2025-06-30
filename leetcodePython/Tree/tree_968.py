from enum import Enum
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CoverState(Enum):
    NotCover = 0
    Covered = 1
    Camera = 2


class Solution:

    def __init__(self):
        self._cameras = 0

    def _checkCover(self, root: Optional[TreeNode]) -> CoverState:
        if not root:
            return CoverState.Covered

        leftState = self._checkCover(root.left)
        rightState = self._checkCover(root.right)

        if leftState == CoverState.NotCover or rightState == CoverState.NotCover:
            self._cameras += 1
            return CoverState.Camera

        if leftState == CoverState.Camera or rightState == CoverState.Camera:
            return CoverState.Covered

        return CoverState.NotCover

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self._cameras = 0
        if self._checkCover(root) == CoverState.NotCover:
            self._cameras += 1
        return self._cameras
