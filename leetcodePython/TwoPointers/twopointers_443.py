from typing import List


class Solution:
    def _put_count(self, chars: List[str], start_i: int, count_str: str) -> int:
        for ch in count_str:
            chars[start_i] = ch
            start_i += 1
        return start_i


    def compress(self, chars: List[str]) -> int:
        ans_i = 0
        ch_count = 1
        curr_ch = ''
        # test [a,a,b]
        for ch_i in range(len(chars)):
            if curr_ch == chars[ch_i]:
                ch_count += 1
                continue
            if ch_count > 1:
                ans_i = self._put_count(chars, ans_i, str(ch_count))
                ch_count = 1
            curr_ch = chars[ch_i]
            chars[ans_i] = curr_ch
            ans_i += 1

        if ch_count > 1:
            ans_i = self._put_count(chars, ans_i, str(ch_count))
        return ans_i