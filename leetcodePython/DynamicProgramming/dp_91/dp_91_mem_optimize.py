class Solution:
    def numDecodings(self, s: str) -> int:
        ways2CharsBefore = 1
        ways1CharBefore = 1

        if s[0] == '0':
            ways1CharBefore = 0
        currentWays = ways1CharBefore

        for charCount in range(2, len(s) + 1):
            charIndex = charCount - 1
            currentWays = 0
            if s[charIndex] != '0':
                currentWays = ways1CharBefore
            twoDigitStr = s[charIndex-1:charIndex+1]
            if 10 <= int(twoDigitStr) <= 26:
                currentWays += ways2CharsBefore
            ways1CharBefore, ways2CharsBefore = currentWays, ways1CharBefore
        return currentWays






