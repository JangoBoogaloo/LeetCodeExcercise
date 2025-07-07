from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        maxNum = int(sqrt(c))
        minNum = 0
        while minNum <= maxNum:
            sqrSum = minNum * minNum + maxNum * maxNum
            if sqrSum < c:
                minNum += 1
            elif sqrSum > c:
                maxNum -= 1
            else:
                return True
        return False
