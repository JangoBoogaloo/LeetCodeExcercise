from typing import List


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden_set = set(forbidden)
        left_bound = 0
        result = 0
        for right in range (len(word)):
            for left in range (max(left_bound,right-10),right+1):
                if word[left:right+1] in forbidden_set:
                    left_bound = left+1
            result = max(result,right-left_bound+1)
        return result