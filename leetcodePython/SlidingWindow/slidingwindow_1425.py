from typing import List
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