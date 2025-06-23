class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        decreaseIndex = len(digits) -1
        while decreaseIndex > 0 and digits[decreaseIndex-1] >= digits[decreaseIndex]:
            decreaseIndex -= 1
        if decreaseIndex == 0:
            return -1
        smallerIndex = decreaseIndex - 1
        biggerIndex = len(digits) -1
        while digits[biggerIndex] <= digits[smallerIndex]:
            biggerIndex -= 1
        digits[biggerIndex], digits[smallerIndex] = digits[smallerIndex], digits[biggerIndex]
        digits[decreaseIndex:] = digits[len(digits)-1:decreaseIndex-1:-1]
        ans = int("".join(digits))
        LIMIT_32_BIT = 1<<31
        return ans if ans < LIMIT_32_BIT else -1