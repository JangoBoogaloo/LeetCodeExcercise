from bisect import bisect_right

class HitCounter:
    def __init__(self):
        self._hitTime = []

    def hit(self, timestamp: int) -> None:
        self._hitTime.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        indexOfTime = bisect_right(self._hitTime, timestamp - 300)
        return len(self._hitTime) - indexOfTime






import pytest


@pytest.mark.parametrize("actions, expect",
[
    ([("hit", 1), ("hit", 2), ("getHit", 300)], 2),
    ([("hit", 1), ("hit", 2), ("getHit", 301)], 1),
])
def test_HitCounter(actions, expect):
    ht = HitCounter()
    for action, time in actions:
        if action == "hit":
            ht.hit(time)
        else:
            assert ht.getHits(time) == expect
