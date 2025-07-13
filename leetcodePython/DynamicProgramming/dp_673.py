from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        longestLengthEndAt = [1] * len(nums)
        countEndAt = [1] * len(nums)

        for right in range(1, len(nums)):
            for left in range(right):
                if nums[left] < nums[right]:
                    newLength = longestLengthEndAt[left] + 1
                    if newLength > longestLengthEndAt[right]:
                        longestLengthEndAt[right] = newLength
                        countEndAt[right] = countEndAt[left]
                    elif newLength == longestLengthEndAt[right]:
                        countEndAt[right] = countEndAt[right] + countEndAt[left]
        maxLength = max(longestLengthEndAt)
        answer = 0
        for i in range(len(longestLengthEndAt)):
            if longestLengthEndAt[i] == maxLength:
                answer += countEndAt[i]
        return answer
