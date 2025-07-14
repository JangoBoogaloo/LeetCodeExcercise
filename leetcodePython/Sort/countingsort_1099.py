from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        numRange = [0] * 1001
        for num in nums:
            numRange[num] += 1
        small, big = 1, min(1000, k)
        answer = -1
        while small <= big:
            if small + big < k and numRange[big]:
                count = 1 if small == big else 0
                if numRange[small] > count:
                    answer = max(answer, small + big)
                small += 1
            else:
                big -= 1
        return answer
