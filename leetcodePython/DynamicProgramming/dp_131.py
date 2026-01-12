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










import pytest

target = Solution()
testCases = [
    ("a", [["a"]]),
    ("aa", [["a", "a"], ["aa"]]),
    ("aaa", [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]),
]
@pytest.mark.parametrize("txt, expect", testCases)
def test_131_partion(txt, expect):
    actual = target.partition(txt)
    for a in actual:
        assert a in expect
    for e in expect:
        assert e in actual