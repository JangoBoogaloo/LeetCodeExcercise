from bisect import bisect_right

class SnapshotArray:
    _MAX = 10**9
    def __init__(self, length: int):
        self._snapId = 0
        self._data = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        snapId, _ = self._data[index][-1]
        if snapId != self._snapId:
            self._data[index].append((self._snapId, val))
        else:
            self._data[index][-1] = (self._snapId, val)

    def snap(self) -> int:
        self._snapId += 1
        return self._snapId - 1

    def get(self, index: int, snap_id: int) -> int:
        snapIndex = bisect_right(self._data[index], (snap_id, self._MAX)) - 1
        _, value = self._data[index][snapIndex]
        return value








