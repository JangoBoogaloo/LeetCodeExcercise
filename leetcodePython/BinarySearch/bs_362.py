from bisect import bisect_right

class HitCounter:
    def __init__(self):
        self._hitTime = []

    def hit(self, timestamp: int) -> None:
        self._hitTime.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        indexOfTime = bisect_right(self._hitTime, timestamp - 300)
        return len(self._hitTime) - indexOfTime






