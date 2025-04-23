class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        longestEndAtChar = [0] * 26
        for ch in s:
            chValue = ord(ch) - ord('a')
            minValue = max(0, chValue - k)
            maxValue = min(chValue + k, 25)
            longestEndAtChar[chValue] = max(longestEndAtChar[minValue:maxValue+1]) + 1
        return max(longestEndAtChar)
