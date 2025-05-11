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


class SolutionSlidingWindowBinarySearch:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Base case
        if len(arr) == k:
            return arr

        # Find the closest element and initialize two pointers
        left = bisect_left(arr, x) - 1
        right = left + 1
        while right - left - 1 < k:
            if left == -1:
                right += 1
            elif right == len(arr):
                left -= 1
            elif abs(arr[left]-x) < abs(arr[right]-x):
                left -= 1
            else:
                right += 1
        return arr[left+1:right]

class SolutionLeftBoundBinarySearch:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize binary search bounds
        left = 0
        right = len(arr) - k

        # Binary search against the criteria described
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]


if __name__ == "__main__":
    sol = SolutionSlidingWindow()
    ans = sol.findClosestElements([0,1,1,1,2,3,6,7,8,9], 9, 4)
    print(ans)