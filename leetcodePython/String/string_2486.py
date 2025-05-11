class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        tIndex = 0
        for ch in s:
            if tIndex == len(t):
                return 0
            if ch == t[tIndex]:
                tIndex += 1
        return len(t) - tIndex