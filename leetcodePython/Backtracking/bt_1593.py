class SolutionBacktrack:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        return self._maxCountAt(0, s, seen)

    def _maxCountAt(self, start: int, s: str, seen: set) -> int:
        if start == len(s):
            return 0
        maxCount = 0
        for end in range(start + 1, len(s) + 1):
            sub_str = s[start:end]
            if sub_str in seen:
                continue
            seen.add(sub_str)
            maxCount = max(maxCount, 1 + self._maxCountAt(end, s, seen))
            seen.remove(sub_str)
        return maxCount


class SolutionBacktrackPrune:
    _maxCount = 0

    def maxUniqueSplit(self, s: str) -> int:
        self._maxCount = 0
        seen = set()

        def countAtIndex(start: int, count: int) -> None:
            if count + (len(s) - start) <= self._maxCount:
                return
            if start == len(s):
                self._maxCount = max(self._maxCount, count)
                return
            for end in range(start+1, len(s)+1):
                sub_str = s[start:end]
                if sub_str in seen:
                    continue
                seen.add(sub_str)
                countAtIndex(end, count+1)
                seen.remove(sub_str)
            return

        countAtIndex(0, 0)
        return self._maxCount
