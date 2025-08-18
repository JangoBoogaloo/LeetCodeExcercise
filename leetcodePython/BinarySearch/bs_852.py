from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr) == 3:
            return 1

        left, right = 1, len(arr) - 2
        while left <= right:
            mid = (left + right) // 2
            if arr[mid-1] > arr[mid]:
                right = mid - 1
            elif arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                return mid
        return -1