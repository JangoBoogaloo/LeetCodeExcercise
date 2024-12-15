from typing import List


class Solution:
    def _isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        allPossible = []

        def backtrack(start: int, palindromes: List[str]) -> None:
            if start == len(s):
                allPossible.append(list(palindromes))
                return
            for end in range(start+1, len(s)+1):
                sub_str = s[start:end]
                if not self._isPalindrome(sub_str):
                    continue
                palindromes.append(sub_str)
                backtrack(end, palindromes)
                palindromes.pop()

        backtrack(0, [])
        return allPossible
