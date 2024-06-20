import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        ch_counts = collections.Counter(s)

        # sorted(ch_counts.items(), key=lambda pair: pair[1], reverse=True)
        # ch_counts.most_common()
        result = ""
        for ch, freq in ch_counts.most_common():
            result += ch*freq
        return result
