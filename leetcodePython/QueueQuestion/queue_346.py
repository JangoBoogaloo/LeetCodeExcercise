import collections


class MovingAverage:

    def __init__(self, size: int):
        self._limit = size
        self._data = collections.deque()
        self._sum = 0

    def next(self, val: int) -> float:
        self._data.append(val)
        self._sum += val
        if len(self._data) > self._limit:
            oldest = self._data.popleft()
            self._sum -= oldest
        return self._sum / len(self._data)


if __name__ == "__main__":
    ma = MovingAverage(3)
    print(ma.next(1))
    print(ma.next(10))
    print(ma.next(3))
    print(ma.next(5))