from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job_info = [(difficulty[i],profit[i]) for i in range(len(difficulty))]
        job_info.sort()
        worker.sort()
        currentMaxProfit = 0
        totalProfit = 0
        jobIndex = 0

        for ability in worker:
            while jobIndex < len(job_info) and job_info[jobIndex][0] <= ability:
                currentMaxProfit = max(currentMaxProfit, job_info[jobIndex][1])
                jobIndex += 1
            totalProfit += currentMaxProfit
        return totalProfit