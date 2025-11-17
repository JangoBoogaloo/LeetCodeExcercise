from typing import List


class SolutionBruteForce:
    @staticmethod
    def _sumPeakAt(index: int, heights: List[int]) -> int:
        total = heights[index]
        currentMin = heights[index]
        for i in range(index+1, len(heights)):
            currentMin = min(heights[i], currentMin)
            total += currentMin
        currentMin = heights[index]
        for i in range(index-1, -1, -1):
            currentMin = min(heights[i], currentMin)
            total += currentMin
        return total

    def maximumSumOfHeights(self, heights: List[int]) -> int:
        maxSum = 0
        for i in range(len(heights)):
            maxSum = max(maxSum, self._sumPeakAt(i, heights))
        return maxSum


class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        acceptedHeightSumAt = [0] * len(heights)
        acceptedHeightSum = 0
        increaseHeightIndexStack = [-1]
        for i in range(len(heights)):
            overHeightSum = 0
            while len(increaseHeightIndexStack) > 1 and heights[i] < heights[increaseHeightIndexStack[-1]]:
                index = increaseHeightIndexStack.pop()
                overHeightSum += (index - increaseHeightIndexStack[-1]) * heights[index]
            acceptedHeightSum += (i - increaseHeightIndexStack[-1])*heights[i]
            acceptedHeightSum -= overHeightSum
            acceptedHeightSumAt[i] = acceptedHeightSum
            increaseHeightIndexStack.append(i)

        increaseHeightIndexStack = [len(heights)]
        acceptedHeightSum = 0
        maxSum = 0
        for i in range(len(heights) -1, -1, -1):
            overHeightSum = 0
            while len(increaseHeightIndexStack) > 1 and heights[i] < heights[increaseHeightIndexStack[-1]]:
                index = increaseHeightIndexStack.pop()
                overHeightSum += (increaseHeightIndexStack[-1] - index) * heights[index]
            acceptedHeightSum += (increaseHeightIndexStack[-1]-i)*heights[i]
            acceptedHeightSum -= overHeightSum
            increaseHeightIndexStack.append(i)
            maxSum = max(maxSum, acceptedHeightSumAt[i] + acceptedHeightSum - heights[i])
        return maxSum
