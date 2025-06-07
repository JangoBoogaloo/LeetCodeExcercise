class Solution:
    def pivotInteger(self, n: int) -> int:
        nSum = (1+n) * n // 2
        prevSum = 0
        for i in range(1, n+1):
            if prevSum * 2 + i == nSum:
                return i
            prevSum += i
        return -1
