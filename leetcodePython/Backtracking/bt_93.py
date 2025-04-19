from typing import List


class Solution:
    @staticmethod
    def _valid(numStr:str) -> bool:
        if len(numStr) > 1 and numStr[0] == "0":
            return False
        if int(numStr) > 255:
            return False
        return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        digits = list(s)
        addresses = []
        currentAddress = []

        def backtrack(startIndex):
            if startIndex > len(digits):
                return
            if startIndex == len(digits):
                if len(currentAddress) == 4:
                    addresses.append(".".join(currentAddress))
                return

            for digitCounts in range(1, 4):
                numberStr = "".join(digits[startIndex:startIndex+digitCounts])
                if not self._valid(numberStr):
                    continue
                currentAddress.append(numberStr)
                nextStart = startIndex + digitCounts
                backtrack(nextStart)
                currentAddress.pop()

        backtrack(0)
        return addresses
