from typing import List


class Solution:
    def _getBestProfit(self, ability, jobInfo) -> int:
        left, right = 0, len(jobInfo) - 1
        bestProfit = 0
        while left <= right:
            mid = (left + right) // 2
            jobProfit, jobDifficulty = jobInfo[mid]
            if jobDifficulty <= ability:
                bestProfit = max(bestProfit, jobProfit)
                right = mid - 1
            else:
                left = mid + 1
        return bestProfit

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobInfo =[(0, 0)] + [(profit[i], difficulty[i]) for i in range(len(difficulty))]
        jobInfo.sort(reverse=True)
        for i in range(len(jobInfo) - 1):
            jobInfo[i+1] = (jobInfo[i+1][0], min(jobInfo[i][1], jobInfo[i+1][1]))

        totalProfit = 0
        for ability in worker:
            totalProfit += self._getBestProfit(ability, jobInfo)
        return totalProfit
