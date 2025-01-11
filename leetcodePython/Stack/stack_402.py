class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stepLeft = k
        remainDigits = []
        for digit in num:
            while stepLeft and remainDigits and digit < remainDigits[-1]:
                remainDigits.pop()
                stepLeft -= 1
            remainDigits.append(digit)

        if stepLeft > 0:
            remainDigits = remainDigits[:-stepLeft]

        numStr = "".join(remainDigits).lstrip('0')
        return numStr if numStr else "0"
