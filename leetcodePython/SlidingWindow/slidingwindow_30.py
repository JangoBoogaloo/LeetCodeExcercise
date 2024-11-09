from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def _slide_window(s: str, needed: Counter, window_size: int, word_len: int, left: int,
                      ans: List[int]) -> None:
        too_freq = False
        match_count = 0
        word_freq = Counter()

        for right in range(left, len(s), word_len):
            if right + word_len > len(s):
                return

            right_word = s[right: right + word_len]
            if right_word not in needed:
                left = right + word_len
                too_freq = False
                match_count = 0
                word_freq = Counter()
                continue

            word_freq[right_word] += 1
            if word_freq[right_word] == needed[right_word]:
                match_count += 1
            while right - left == window_size or too_freq:
                left_word = s[left:left + word_len]
                if word_freq[left_word] == needed[left_word] + 1:
                    too_freq = False
                elif word_freq[left_word] == needed[left_word]:
                    match_count -= 1
                word_freq[left_word] -= 1
                left += word_len
            if match_count == len(needed):
                print(s[left:right+1])
                ans.append(left)

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        needed = Counter(words)
        word_len = len(words[0])
        window_len = len(words) * word_len
        ans = []
        for i in range(word_len):
            self._slide_window(s, needed, window_len, word_len, i, ans)
        return ans


if __name__ == '__main__':
    solution = Solution()
    answer = solution.findSubstring("bcabbcaabbccacacbabccacaababcbb", ["c","b","a","c","a","a","a","b","c", "cb"])
    print(answer)