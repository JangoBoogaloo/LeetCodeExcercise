import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right = int(math.sqrt(c))
        left = 0
        while left <= right:
            curr = left * left + right * right
            if curr < c:
                left += 1
            elif curr > c:
                right -= 1
            else:
                return True

        return False
