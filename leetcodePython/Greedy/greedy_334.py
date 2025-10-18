from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        sequence = [float('inf')] * 3
        for num in nums:
            if num <= sequence[0]:
                sequence[0] = num
            elif num <= sequence[1]:
                sequence[1] = num
            else:
                return True
        return False
