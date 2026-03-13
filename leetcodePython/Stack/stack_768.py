from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        increaseStack = []
        for num in arr:
            largest = num
            while increaseStack and num < increaseStack[-1]:
                largest = max(largest, increaseStack.pop())
            increaseStack.append(largest)
        return len(increaseStack)






