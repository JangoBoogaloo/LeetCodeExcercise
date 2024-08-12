import collections


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        freq = collections.Counter(s)
        sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        min_press = 0
        number = 1
        for ch, count in sorted_freq:
            if number <= 9:
                min_press += count
            elif number <= 18:
                min_press += 2*count
            else:
                min_press += 3*count
            number += 1
        return min_press