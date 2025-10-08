from typing import List

class Solution:
    def _getBestProfit(self, ability, jobInfo) -> int:
        left, right = 0, len(jobInfo) - 1
        bestProfit = 0
        while left <= right:
            mid = (left + right) // 2
            jobDifficulty, jobProfit = jobInfo[mid]
            if jobDifficulty <= ability:
                bestProfit = max(bestProfit, jobProfit)
                left = mid + 1
            else:
                right = mid - 1
        return bestProfit

    def maxProfitAssignment(self, difficulties: List[int], profits: List[int], workers: List[int]) -> int:
        jobInfo =[(difficulties[i], profits[i]) for i in range(len(difficulties))]
        jobInfo.sort()
        optimalProfitJobInfo = [(0, 0)] + jobInfo
        for i in range(len(optimalProfitJobInfo) - 1):
            optimalProfitJobInfo[i + 1] = (optimalProfitJobInfo[i+1][0], max(optimalProfitJobInfo[i][1], optimalProfitJobInfo[i+1][1]))

        totalProfit = 0
        for ability in workers:
            totalProfit += self._getBestProfit(ability, optimalProfitJobInfo)
        return totalProfit