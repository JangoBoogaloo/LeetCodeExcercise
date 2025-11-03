class Solution:
    def numDecodings(self, s: str) -> int:
        waysWithCharCount = [0] * (len(s) + 1)
        waysWithCharCount[0] = 1
        if not s:
            return 1
        if s[0] != '0':
            waysWithCharCount[1] = 1
        for charCount in range(2, len(s) + 1):
            charIndex = charCount - 1
            if s[charIndex] != '0':
                waysWithCharCount[charCount] = waysWithCharCount[charCount - 1]
            twoDigitStr = s[charIndex-1:charIndex+1]
            if 10 <= int(twoDigitStr) <= 26:
                waysWithCharCount[charCount] += waysWithCharCount[charCount - 2]
        return waysWithCharCount[len(s)]






