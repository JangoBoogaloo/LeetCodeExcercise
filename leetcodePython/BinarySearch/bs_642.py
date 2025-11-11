from typing import List
from bisect import bisect_left

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self._freq = {s: t for s, t in zip(sentences, times)}
        self._rank = sorted((-t, s) for t, s in zip(times, sentences))
        self._sortedSentences = []
        self._reset()

    def _reset(self):
        self._txt = []
        self._sortedSentences = [s for _, s in self._rank]


    def input(self, ch: str) -> List[str]:
        if ch != "#":
            self._txt.append(ch)
            currentIndex = len(self._txt) - 1
            sortedSentences = []
            for sentence in self._sortedSentences:
                if len(sentence) > currentIndex and sentence[currentIndex] == ch:
                    sortedSentences.append(sentence)
            self._sortedSentences = sortedSentences
            return self._sortedSentences[:3]
        newSentence = "".join(self._txt)
        if newSentence in self._freq:
            index = bisect_left(self._rank, (-self._freq[newSentence], newSentence))
            self._rank.pop(index)
        else:
            self._freq[newSentence] = 0
        self._freq[newSentence] += 1

        freqNewSentence = (-self._freq[newSentence], newSentence)
        newSentenceIndex = bisect_left(self._rank, freqNewSentence)
        self._rank.insert(newSentenceIndex, freqNewSentence)
        self._reset()
        return []









