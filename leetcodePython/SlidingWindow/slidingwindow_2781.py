from typing import List


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden_set = set(forbidden)

        # forbidden_max_length = max([len(f) for f in forbidden_set])
        forbidden_max_length = 10
        max_length = 0
        valid_left = 0
        for right in range(len(word)):
            left_start = max(valid_left, right - forbidden_max_length)
            for left in range(left_start, right+1):
                if word[left:right+1] in forbidden_set:
                    valid_left = left + 1
            max_length = max(max_length, right - valid_left + 1)
        return max_length
