class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        digits = list(number)
        digitIndex = -1
        for i in range(len(digits)):
            if digits[i] == digit:
                digitIndex = i
                if digitIndex < len(digits) - 1 and digits[digitIndex] < digits[digitIndex + 1]:
                    break
        digits[digitIndex] = ""
        return "".join(digits)
