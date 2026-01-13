from typing import List


class Solution:
    _MATCH_COUNT = 3
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        left, right = 0, len(products) - 1
        res = []
        for i in range(len(searchWord)):
            currChar = searchWord[i]
            while left <= right and (len(products[left]) <= i or products[left][i] != currChar):
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] != currChar):
                right -= 1
            currentMatches = []
            for j in range(min(right - left + 1, self._MATCH_COUNT)):
                currentMatches.append(products[left + j])
            res.append(currentMatches)
        return res









import pytest
target = Solution()

@pytest.mark.parametrize("products, searchWord, expect",
[
    (["a", "ab", "ac"], "a", [["a", "ab", "ac"]]),
    (["aa", "ab", "ac"], "aa", [["aa", "ab", "ac"], ["aa"]]),
    (["ad", "aa", "ab", "ac"], "aa", [["aa", "ab", "ac"], ["aa"]]),
    (["aad", "aa", "aaa", "aab", "aac"], "aaa", [["aa", "aaa", "aab"], ["aa", "aaa", "aab"], ["aaa"]]),
    (["aad", "aa", "aaa", "aab", "aaac"], "aaa", [["aa", "aaa", "aaac"], ["aa", "aaa", "aaac"], ["aaa", "aaac"]]),
])
def test_suggestedProducts(products, searchWord, expect):
    assert target.suggestedProducts(products, searchWord) == expect