from typing import List
from heapq import heappush, heappop


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        num_row_col = []
        for row in range(len(nums)):
            heappush(num_row_col, (nums[row][0], row, 0))
        interval = [0, float("inf")]
        biggest = max(row[0] for row in nums)
        while num_row_col:
            smallest, row, col = heappop(num_row_col)
            if biggest - smallest < interval[1] - interval[0]:
                interval = [smallest, biggest]
            row_data = nums[row]
            if col +1 == len(row_data):
                return interval
            next_data = nums[row][col+1]
            biggest = max(biggest, next_data)
            heappush(num_row_col, (next_data, row, col+1))
        return interval
