from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        needed = Counter(words)
        window_size = len(words)*word_length
        ans = []

        def sliding_window(left: int) -> None:
            used = 0
            excess = False
            word_count = Counter()
            for right in range(left, len(s), word_length):
                if right + word_length > len(s):
                    break
                word = s[right:right+word_length]
                # completely invalid, jump the index, reset everything
                if word not in needed:
                    word_count = Counter()
                    used = 0
                    excess = False
                    left = right + word_length
                else:
                    while right - left == window_size or excess:
                        left_word = s[left:left+word_length]
                        left += word_length
                        word_count[left_word] -= 1
                        if word_count[left_word] == needed[left_word]:
                            excess = False
                        else:
                            used -= 1
                    word_count[word] += 1
                    if word_count[word] > needed[word]:
                        excess = True
                    else:
                        used += 1
                    if used == len(words) and not excess:
                        ans.append(left)

        for i in range(word_length):
            sliding_window(i)
        return ans