import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        ch_counts = collections.Counter(s)
        result = ""
        for ch, freq in ch_counts.most_common():
            result += ch*freq
        return result
