class Solution316:
    def removeDuplicateLetters(self, s: str) -> str:
        increaseChars = []
        seen = set()
        lastIndexOfCh = {}

        for i, c in enumerate(s):
            lastIndexOfCh[c] = i

        for i in range(len(s)):
            if s[i] not in seen:
                while increaseChars and s[i] < increaseChars[-1] and i < lastIndexOfCh[increaseChars[-1]]:
                    seen.discard(increaseChars.pop())
                seen.add(s[i])
                increaseChars.append(s[i])
        return ''.join(increaseChars)


class Solution1081:
    def smallestSubsequence(self, s: str) -> str:
        increaseChars = []
        seen = set()
        lastIndexOfCh = {}

        for i, c in enumerate(s):
            lastIndexOfCh[c] = i

        for i in range(len(s)):
            if s[i] not in seen:
                while increaseChars and s[i] < increaseChars[-1] and i < lastIndexOfCh[increaseChars[-1]]:
                    seen.discard(increaseChars.pop())
                seen.add(s[i])
                increaseChars.append(s[i])
        return ''.join(increaseChars)
