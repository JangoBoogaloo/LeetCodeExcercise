from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self._data = {}
        return

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._data:
            self._data[key] = []
        self._data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._data:
            return ""
        index = bisect_right(self._data[key], timestamp, key=lambda x: x[0]) - 1
        if index < 0:
            return ""
        if self._data[key][index][0] > timestamp:
            return ""
        return self._data[key][index][1]









import pytest

@pytest.mark.parametrize("setData, getData, expect",
[
    ([("KeyA", "ValueA", 10),
      ("KeyA", "ValueB", 20),
      ("KeyA", "ValueC", 30)], ("KeyA", 19), "ValueA"),
    ([("KeyA", "ValueA", 10),
      ("KeyA", "ValueB", 20),
      ("KeyA", "ValueC", 30)], ("KeyA", 20), "ValueB"),
    ([("KeyA", "ValueA", 10),
      ("KeyA", "ValueB", 20),
      ("KeyA", "ValueC", 30)], ("KeyA", 9), ""),
    ([("KeyA", "ValueA", 10),
      ("KeyA", "ValueB", 20),
      ("KeyA", "ValueC", 30)], ("KeyB", 30), "")

])
def test_checkType(setData, getData, expect):
    tm = TimeMap()
    for key, value, time in setData:
        tm.set(key, value, time)
    getKey, getTime = getData
    assert tm.get(getKey, getTime) == expect