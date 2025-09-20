from collections import Counter


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        countAtMask = Counter()
        countAtMask[0] = 1

        mask = 0
        maxBitRange = 0
        for ch in word:
            chBit = 1 << (ord(ch) - ord('a'))
            mask = mask ^ chBit
            maxBitRange = max(maxBitRange, mask)
            countAtMask[mask] += 1
        maxBitRange += 1
        result = 0
        for msk in range(maxBitRange):
            if not countAtMask[msk]:
                continue
            maskCount = countAtMask[msk]
            subStringCount = maskCount * (maskCount - 1) // 2
            result += subStringCount

            bit = 1
            while bit < maxBitRange:
                if msk & bit:
                    subStringCount = countAtMask[msk] * countAtMask[msk ^ bit]
                    result += subStringCount
                bit <<= 1
        return result









