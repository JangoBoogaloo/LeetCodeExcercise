import math
from typing import List


class Solution:

    '''
    To make all bags with balls smaller than value, how much operation do we need
    '''
    def _getOperations(self, nums: List[int], value: int) -> int:
        operations = 0
        for balls in nums:
            # consider 6 balls with value 3, you only need 1 move
            operations += (balls - 1) // value
        return operations

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left = 1
        right = max(nums)

        while left < right:
            guess_penalty = (left + right) // 2
            if self._getOperations(nums, guess_penalty) > maxOperations:
                left = guess_penalty + 1
            else:
                right = guess_penalty
        return left