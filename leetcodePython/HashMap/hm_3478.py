from typing import List
from heapq import heappush, heappop

class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        sortedNum1Index = sorted(range(len(nums1)), key= lambda i: nums1[i])
        currSum, prevNum1, prevSum = 0, 0, 0
        minHeap = []
        answer = [0] * len(nums1)
        for index in sortedNum1Index:
            num1, num2 = nums1[index], nums2[index]
            if prevNum1 < num1:
                prevSum = currSum
            answer[index] = prevSum
            prevNum1 = num1
            currSum += num2
            if len(minHeap) == k:
                heappush(minHeap, num2)
                currSum -= heappop(minHeap)
            else:
                heappush(minHeap, num2)
        return answer