from typing import List


class SolutionMonotonicStack:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        increaseStack = []
        for num in arr:
            largest = num
            while increaseStack and num < increaseStack[-1]:
                largest = max(largest, increaseStack.pop())
            increaseStack.append(largest)
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
