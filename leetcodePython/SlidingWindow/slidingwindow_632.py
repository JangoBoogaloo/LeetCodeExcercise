from typing import List
import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # start our heap with the first element from every single list
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(heap)
        ans = [0, float("inf")]
        # maximum within the smallest data in each row
        biggest = max(row[0] for row in nums)

        while heap:
            # get current smallest data from priority queue
            smallest, r, c = heapq.heappop(heap)
            # if this data have smaller range, update answer
            if biggest - smallest < ans[1] - ans[0]:
                ans = [smallest, biggest]
            data_list = nums[r]

            # if we hit this condition, we are going to get out of range of a row, that will break the requirement
            if c + 1 == len(data_list):
                return ans
            next_num = nums[r][c + 1]
            biggest = max(biggest, next_num)

            heapq.heappush(heap, (next_num, r, c + 1))
