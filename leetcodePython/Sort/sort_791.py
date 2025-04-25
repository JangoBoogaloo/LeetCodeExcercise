import collections
from functools import cmp_to_key


class SolutionCounter:
    def customSortString(self, order: str, s: str) -> str:
        ch_count = collections.Counter(s)
        ans = ''
        for ch in order:
            if ch in ch_count:
                ans = ans + ch * ch_count[ch]
                ch_count[ch] = 0

        for key in ch_count:
            if ch_count[key] > 0:
                ans = ans + key * ch_count[key]
        return ans


class SolutionSort:
    def customSortString(self, order: str, s: str) -> str:
        s_list = list(s)

        def compare(a: str, b: str) -> int:
            a_i = order.index(a) if a in order else len(order)
            b_i = order.index(b) if b in order else len(order)
            return a_i - b_i

        s_list.sort(key=cmp_to_key(compare))

        return ''.join(s_list)
