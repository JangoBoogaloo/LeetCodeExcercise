class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        remainRemoval = k
        increaseDigits = []
        for digit in num:
            while remainRemoval and increaseDigits and digit < increaseDigits[-1]:
                increaseDigits.pop()
                remainRemoval -= 1
            increaseDigits.append(digit)

        if remainRemoval > 0:
            increaseDigits = increaseDigits[:-remainRemoval]

        numStr = "".join(increaseDigits).lstrip('0')
        return numStr if numStr else "0"
