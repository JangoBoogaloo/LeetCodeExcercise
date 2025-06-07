from typing import List


class Solution:
    _REQUIRE_BLOCKS = 4
    _DIGITS_PER_BLOCK = 3

    @staticmethod
    def _leadingZero(numStr:str) -> bool:
        if len(numStr) > 1 and numStr[0] == "0":
            return True
        return False

    @staticmethod
    def _valid(numStr:str) -> bool:
        if int(numStr) > 255:
            return False
        return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        digits = list(s)
        addresses = []
        addressBlocks = []

        def backtrack(startIndex):
            if startIndex > len(digits):
                return
            if startIndex == len(digits):
                if len(addressBlocks) == self._REQUIRE_BLOCKS:
                    addresses.append(".".join(addressBlocks))
                return
            remainMaxDigits = (self._REQUIRE_BLOCKS - len(addressBlocks)) * self._DIGITS_PER_BLOCK
            if len(digits) - startIndex > remainMaxDigits:
                return

            for digitCounts in range(1, 1+self._DIGITS_PER_BLOCK):
                numberStr = "".join(digits[startIndex:startIndex+digitCounts])
                if self._leadingZero(numberStr):
                    break
                if not self._valid(numberStr):
                    continue
                addressBlocks.append(numberStr)
                nextStart = startIndex + digitCounts
                backtrack(nextStart)
                addressBlocks.pop()

        backtrack(0)
        return addresses
