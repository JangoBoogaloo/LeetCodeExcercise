from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        oddCount, evenCount, alternateCount = 0, 0, 1
        prevDivisibleByTwo = nums[0] % 2
        for num in nums:
            divisibleByTwo = num % 2
            if divisibleByTwo:
                evenCount += 1
            else:
                oddCount += 1
            if prevDivisibleByTwo != divisibleByTwo:
                alternateCount += 1
            prevDivisibleByTwo = divisibleByTwo
        return max(oddCount, evenCount, alternateCount)

