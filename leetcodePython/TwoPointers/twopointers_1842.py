from typing import Optional


class Solution:
    def nextPalindrome(self, num: str) -> str:
        if len(num) < 4:
            return ""
        halfIndex = len(num) // 2
        center = ""
        if len(num) % 2:
            center = num[halfIndex]
        half = num[:halfIndex]
        greaterHalf = self._nextGreaterNumber(half)
        if not greaterHalf:
            return ""
        return greaterHalf + center + greaterHalf[::-1]

    @staticmethod
    def _nextGreaterNumber(num:str) -> Optional[str]:
        digits = list(num)
        decreaseIndex = len(digits) - 1
        while decreaseIndex > 0 and digits[decreaseIndex-1] >= digits[decreaseIndex]:
            decreaseIndex -= 1
        if decreaseIndex == 0:
            return None
        smallerIndex = decreaseIndex - 1
        largerIndex = len(digits) - 1
        while digits[largerIndex] <= digits[smallerIndex]:
            largerIndex -= 1
        digits[smallerIndex], digits[largerIndex] = digits[largerIndex], digits[smallerIndex]
        digits[decreaseIndex:] = digits[len(digits)-1:decreaseIndex-1:-1]
        return "".join(digits)
