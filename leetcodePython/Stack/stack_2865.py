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





if __name__ == '__main__':
    solution = SolutionBruteForce()
    print(solution.maximumSumOfHeights([3,2,5,5,2,3]))