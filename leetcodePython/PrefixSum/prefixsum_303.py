from typing import List


class NumArray:
    _sums = []

    def __init__(self, nums: List[int]):
        if len(nums) == 0:
            return
        self._sums = [nums[0]]
        for i in range(1, len(nums)):
            self._sums.append(self._sums[i - 1] + nums[i])
        print(self._sums)

    def sumRange(self, left: int, right: int) -> int:
        if len(self._sums) == 0:
            return 0
        if left == 0:
            return self._sums[right]
        return self._sums[right] - self._sums[left - 1]


if __name__ == "__main__":
    arr = [-2, 0, 3, -5, 2, -1]
    print(arr)
    num_arr = NumArray(arr)
    data = num_arr.sumRange(0, 2)
    print(data)
