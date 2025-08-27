from typing import List
from collections import deque

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        level = deque([(0, 0)])
        ans = []
        while level:
            row, col = level.popleft()
            ans.append(nums[row][col])

            if col == 0 and row + 1 < len(nums):
                level.append((row+1, col))
            if col + 1 < len(nums[row]):
                level.append((row, col+1))
        return ans







