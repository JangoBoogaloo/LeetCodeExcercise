from collections import defaultdict
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        allPartitions = []
        isPalindrome = defaultdict(bool)
        def backtrack(startIndex: int, currentPalindromes: List[str]):
            if startIndex == len(s):
                allPartitions.append(list(currentPalindromes))
                return
            for end in range(startIndex, len(s)):
                if s[startIndex] == s[end] and (end - startIndex <= 2 or isPalindrome[(startIndex + 1, end-1)]):
                    isPalindrome[(startIndex, end)] = True
                    currentPalindromes.append(s[startIndex: end+1])
                    backtrack(end+1, currentPalindromes)
                    currentPalindromes.pop()

        backtrack(0, [])
        return allPartitions










