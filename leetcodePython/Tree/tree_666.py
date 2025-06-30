from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    _sum = 0

    def _toDigits(self, num: int) -> List[int]:
        ans = deque()
        while num > 0:
            ans.appendleft(num%10)
            num //= 10
        return list(ans)

    def pathSum(self, nums: List[int]) -> int:
        locationValueMap = {}
        self._sum = 0
        for num in nums:
            depth, pos, value = self._toDigits(num)
            locationValueMap[(depth, pos)] = value
        self._isValid(1, 1, 0, locationValueMap)
        return self._sum

    def _isValid(self, depth:int, pos:int, ancestorsSum: int, locationValueMap: dict) -> bool:
        location = (depth, pos)
        if location not in locationValueMap:
            return False
        ancestorsSum += locationValueMap[location]
        left = self._isValid(depth + 1, pos * 2 - 1, ancestorsSum, locationValueMap)
        right = self._isValid(depth + 1, pos * 2, ancestorsSum, locationValueMap)
        if not left and not right:
            self._sum += ancestorsSum
        return True
