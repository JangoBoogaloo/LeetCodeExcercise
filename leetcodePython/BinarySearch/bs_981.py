import bisect
import collections
from typing import List


class Data:
    def __init__(self, time: int, value: str):
        self.time = time
        self.value = value

class TimeMap:

    def __init__(self):
        self._timemap = collections.defaultdict(List[Data])

    def set(self, key: str, value: str, timestamp: int) -> None:
        data = Data(timestamp, value)
        if key not in self._timemap:
            self._timemap[key] = []
        bisect.insort_right(self._timemap[key], data, key=lambda d: d.time)

    def get(self, key: str, timestamp: int) -> str:
        if not self._timemap[key]:
            return ''
        data = Data(timestamp, '')
        index = bisect.bisect_right(self._timemap[key], timestamp, key=lambda d: d.time)
        if index == 0:
            return ''
        return self._timemap[key][index-1].value


if __name__ == '__main__':
    timeMap = TimeMap()
    timeMap.set('foo', 'b', 1)
    timeMap.set('foo', 'a', 1)
    a = timeMap.get('foo', 1)
    print(a)
