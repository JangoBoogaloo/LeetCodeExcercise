import bisect


class SnapshotArray_BruteForce:
    def __init__(self, length: int):
        self._snap_id = -1
        self._array = [0] * length
        self.snap_info = {}

    def set(self, index: int, val: int) -> None:
        self._array[index] = val

    def snap(self) -> int:
        self._snap_id += 1
        self.snap_info[self._snap_id] = [val for val in self._array]
        return self._snap_id

    def get(self, index: int, snap_id: int) -> int:
        return self.snap_info[snap_id][index]


class SnapshotArray:
    def __init__(self, length: int):
        self._snap_id = 0
        # we can not do [[(0, 0)]] * len(length), it will use [(0, 0)] as a reference copy instead of deep copy
        self._array = [[(0, 0)] for _ in range(length)]
        self.snap_info = {}

    def set(self, index: int, val: int) -> None:
        snap_id, _ = self._array[index][-1]
        # we only add new data with new id, old id we change value
        if snap_id != self._snap_id:
            self._array[index].append((self._snap_id, val))
        else:
            self._array[index][-1] = (snap_id, val)

    def snap(self) -> int:
        self._snap_id += 1
        return self._snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        data_at_index = self._array[index]
        snap_idx = bisect.bisect_right(data_at_index, (snap_id, 10**9))
        _, data = data_at_index[snap_idx-1]
        return data
