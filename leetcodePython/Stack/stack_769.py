from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        increaseStack = []
        for num in arr:
            currentLargest = num
            while increaseStack and num < increaseStack[-1]:
                lastLargest = increaseStack.pop()
                currentLargest = max(currentLargest, lastLargest)
            increaseStack.append(currentLargest)
        return len(increaseStack)






