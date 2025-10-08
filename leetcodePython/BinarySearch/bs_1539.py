from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            midIndex = (left + right) // 2
            expectNumber = midIndex + 1
            actualNumber = arr[midIndex]
            if actualNumber < expectNumber + k:
                left = midIndex + 1
            else:
                right = midIndex - 1
        return left + k








