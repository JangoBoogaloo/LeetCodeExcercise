from collections import Counter


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        frequency = Counter(s)
        mapCount = [0] * 9
        pressCount = 0
        index = 0
        for ch, freq in frequency.most_common():
            mapCount[index] += 1
            pressCount += freq * mapCount[index]
            index = (index+1) % 9
        return pressCount






