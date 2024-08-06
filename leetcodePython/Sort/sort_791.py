import collections


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
                ans = ans + key*ch_count[key]
        return ans
