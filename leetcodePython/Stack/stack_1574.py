from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        removalLeftBoundary = 0
        while removalLeftBoundary < len(arr) - 1 and arr[removalLeftBoundary] < arr[removalLeftBoundary + 1]:
            removalLeftBoundary += 1
        if removalLeftBoundary == len(arr) - 1:
            return 0
        removeRightDecreaseStack = [len(arr) - 1]
        for r in range(len(arr) - 2, removalLeftBoundary, -1):
            if arr[r] > arr[r+1]:
                break
            removeRightDecreaseStack.append(r)

        removeSubArrayLength = min(len(arr) -1 - removalLeftBoundary, removeRightDecreaseStack[-1])
        for removalLeft in range(removalLeftBoundary+1):
            while removeRightDecreaseStack and arr[removalLeft] > arr[removeRightDecreaseStack[-1]]:
                removeRightDecreaseStack.pop()
            if removeRightDecreaseStack:
                removalRight = removeRightDecreaseStack[-1]
                removeSubArrayLength = min(removeSubArrayLength, removalRight - removalLeft - 1)
        return removeSubArrayLength






