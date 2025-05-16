import heapq
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        pq = [(-count, num) for num, count in Counter(nums).items()]
        print(pq)
        heapq.heapify(pq)
        ans = []
        while pq and len(ans) < k:
            ans.append(heapq.heappop(pq)[1])
        return ans

if __name__ == "__main__":
    sol = Solution()
    sol.topKFrequent([3,1,1,1,2,2], 2)