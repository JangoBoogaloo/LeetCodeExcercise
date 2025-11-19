from typing import List

class Solution:
    def findPeakElement(self, nums: List[float]) -> float:
        nums.append(float('-inf'))
        left, right = 0, len(nums)-1
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                answer = mid
                right = mid - 1
        return answer






