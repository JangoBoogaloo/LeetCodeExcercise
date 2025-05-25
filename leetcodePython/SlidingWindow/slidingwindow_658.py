from bisect import bisect_left
from typing import List


class SolutionSlidingWindow:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        window_sum, left = 0, 0
        min_left, min_right = 0, 0
        min_sum = float('inf')

        for right in range(len(arr)):
            window_sum += abs(arr[right]-x)
            while right-left+1 > k:
                window_sum -= abs(arr[left]-x)
                left += 1
            if right-left+1 == k:
                if window_sum < min_sum:
                    min_sum = window_sum
                    min_left = left
                    min_right = right
        return arr[min_left:min_right+1]


class SolutionLeftBoundBinarySearch:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        # guess the left boundary for k_window
        right = len(arr) - k
        while left < right:
            k_left = (left + right) // 2
            k_right = k_left + k
            if x - arr[k_left] > arr[k_right] - x:
                left = k_left + 1
            else:
                right = k_left
        return arr[left:left + k]
