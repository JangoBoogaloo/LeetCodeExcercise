from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job_info = [(difficulty[i],profit[i]) for i in range(len(difficulty))]
        job_info.sort()
        worker.sort()
        net_profit, max_profit, job_i = 0,0,0

        # workers sorted by ability, so worker is more powerful in next iteration
        for ability in worker:
            # loop through difficulty
            while job_i < len(difficulty) and ability >= job_info[job_i][0]:
                # to see a potential bigger profit, if not bigger than existing record
                max_profit = max(max_profit, job_info[job_i][1])
                # job profit recorded, we check next, we dont need to loop back to beginning, as it is already recorded
                job_i += 1

            # we might be using a previous max profit, and guarantee affordable difficulty, as worker more powerful
            net_profit += max_profit

        return net_profit
