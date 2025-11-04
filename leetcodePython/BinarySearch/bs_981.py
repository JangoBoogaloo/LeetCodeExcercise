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









