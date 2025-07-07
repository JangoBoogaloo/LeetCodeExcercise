from typing import List


class Solution:
    def _isPalindrome(self, txt: str) -> bool:
        left, right = 0, len(txt) - 1
        while left < right:
            if txt[left] != txt[right]:
                return False
            left += 1
            right -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        allPartitions = []
        def backtrack(startIndex: int, currentPalindromes: List[str]):
            if startIndex == len(s):
                allPartitions.append(list(currentPalindromes))
                return
            for end in range(startIndex+1, len(s)+1):
                subStr = s[startIndex:end]
                if not self._isPalindrome(subStr):
                    continue
                currentPalindromes.append(subStr)
                backtrack(end, currentPalindromes)
                currentPalindromes.pop()
        backtrack(0, [])
        return allPartitions