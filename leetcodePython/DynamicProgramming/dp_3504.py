class Solution:
    def _isPalindrome(self, txt: str, left:int, right:int) -> bool:
        if left >= right:
            return True
        return txt[left] == txt[right] and self._isPalindrome(txt, left+1, right-1)

    @staticmethod
    def _palindromeExpandCount(leftSub: str, rightSub: str, leftStart: int, rightEnd: int) -> int:
        count = 0
        while leftStart >=0 and rightEnd < len(rightSub) and leftSub[leftStart] == rightSub[rightEnd]:
            leftStart -= 1
            rightEnd += 1
            count+= 1
        return count

    def longestPalindrome(self, s: str, t: str) -> int:
        if s == t:
            return 2*len(s)
        maxLength = 0
        leftSubStrPalLength = [0] * len(s)
        for start in range(len(s)):
            for end in range(start, len(s)):
                if not self._isPalindrome(s, start, end):
                    continue
                leftSubStrPalLength[start] = max(leftSubStrPalLength[start], end-start+1)
                maxLength = max(maxLength, leftSubStrPalLength[start])

        rightSubStrPalLength = [0] * len(t)
        for end in range(len(t)):
            for start in range(end+1):
                if not self._isPalindrome(t, start, end):
                    continue
                rightSubStrPalLength[end] = max(rightSubStrPalLength[end], end-start+1)
                maxLength = max(maxLength, rightSubStrPalLength[end])

        for leftIndex in range(len(s)):
            for rightIndex in range(len(t)):
                if s[leftIndex] == t[rightIndex]:
                    expandCount = self._palindromeExpandCount(s, t, leftIndex, rightIndex)
                    extra = 0
                    if leftIndex + 1 < len(s):
                        extra = max(extra, leftSubStrPalLength[leftIndex + 1])
                    if rightIndex - 1 >= 0:
                        extra = max(extra, rightSubStrPalLength[rightIndex - 1])
                    maxLength = max(maxLength, 2 * expandCount + extra)
        return maxLength
