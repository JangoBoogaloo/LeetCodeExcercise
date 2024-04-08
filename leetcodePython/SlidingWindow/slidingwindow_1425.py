from typing import List
from collections import deque
import heapq


class SolutionPriorityQueue:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap = [(-nums[0], 0)]
        ans = nums[0]

        for i in range(1, len(nums)):
            # if the maximum sum's including index is out of k range, remove it
            while i - heap[0][1] > k:
                heapq.heappop(heap)
            # the maximum sum including i is a positive sum plus i or the data in i itself
            curr = max(0, -heap[0][0]) + nums[i]
            # compare with current answer
            ans = max(ans, curr)
            # save your current index sum
            heapq.heappush(heap, (-curr, i))

        return ans


class SolutionMonotonicDeque:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        index_queue = deque()
        dp = [0] * len(nums)

        for i in range(len(nums)):
            if index_queue and i - index_queue[0] > k:
                index_queue.popleft()

            dp[i] = (dp[index_queue[0]] if index_queue else 0) + nums[i]
            '''
            The reason we want to remove elements that are less than dp[i] is because dp[i] comes after those elements. 
            Thus, those elements will be out of range before dp[i], and because dp[i] is greater than them, 
            there is no chance those elements will ever be the maximum value in the last k indices anymore.
            '''
            while index_queue and dp[index_queue[-1]] < dp[i]:
                index_queue.pop()
            if dp[i] > 0:
                index_queue.append(i)
        return max(dp)