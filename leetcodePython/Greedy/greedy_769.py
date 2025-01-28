from typing import List


class SolutionMonotonicStack:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        increaseStack = []
        for i in range(len(arr)):
            if not increaseStack or arr[i] > increaseStack[-1]:
                increaseStack.append(arr[i])
            else:
                maxNum = increaseStack[-1]
                while increaseStack and arr[i] < increaseStack[-1]:
                    increaseStack.pop()
                increaseStack.append(maxNum)
        return len(increaseStack)


class SolutionMaxElement:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sortedCurrentSum = 0
        currSum = 0
        chunks = 0
        for i in range(len(arr)):
            sortedCurrentSum += i
            currSum += arr[i]
            if currSum == sortedCurrentSum:
                chunks += 1
        return chunks


class SolutionPrefixSum:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        currMax = 0
        chunks = 0
        for i in range(len(arr)):
            currMax = max(currMax, arr[i])
            max_i = i
            if currMax == max_i:
                chunks += 1
        return chunks
