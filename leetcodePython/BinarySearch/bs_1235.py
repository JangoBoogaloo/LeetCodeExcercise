import heapq
from typing import List


class SolutionDP:
    def __init__(self):
        self._job_memo = [0] * 50001

    @staticmethod
    def _findNextJobIndex(startTimes: List[int], lastEndTime: int) -> int:
        left, right = 0, len(startTimes) - 1
        next_index = -1
        while left <= right:
            mid = (left + right) // 2
            if startTimes[mid] < lastEndTime:
                left = mid + 1
            else:
                next_index = mid
                right = mid - 1
        return next_index

    def _findMaxProfit(self, jobs: List[tuple[int, int, int]], startTimes: List[int]) -> int:
        # reverse bottom up find max benefit for jobs.
        # Start from end, for each job consider if we use current job profit, or next job profit
        for i in range(len(startTimes) - 1, -1, -1):
            _, endTime, profit = jobs[i]

            next_job_index = self._findNextJobIndex(startTimes, endTime)

            if next_job_index != -1:  # next job no conflict, add profit for using next job
                profit += self._job_memo[next_job_index]

            if i == len(startTimes) - 1:  # last job, no need to calculate other situation
                self._job_memo[i] = profit
            else:  # use this job's profit? Or use next job's profit (next job profit already cumulated maximum)
                self._job_memo[i] = max(profit, self._job_memo[i + 1])
        return self._job_memo[0]

    def jobScheduling(self, startTimes: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []

        for i in range(len(profit)):
            job = (startTimes[i], endTime[i], profit[i])
            jobs.append(job)

        jobs.sort()

        for i in range(len(profit)):
            startTimes[i], _, _ = jobs[i]

        return self._findMaxProfit(jobs, startTimes)


class SolutionPriorityQueue:
    def _findMaxProfit(self, jobs: List[tuple[int, int, int]]) -> int:
        job_chain_heap: List[tuple[int, int]]  # (end_time, profit)
        job_chain_heap = []
        prev_max_profit = 0
        for i in range(len(jobs)):
            new_start, end, profit_i = jobs[i]
            while job_chain_heap:
                prev_end, prev_profit = job_chain_heap[0]
                if new_start < prev_end:  # start is earlier than end, we can't merge in a chain
                    break
                prev_max_profit = max(prev_max_profit, prev_profit)
                heapq.heappop(job_chain_heap)

            chained_jobs_i = (end, prev_max_profit+profit_i)
            heapq.heappush(job_chain_heap, chained_jobs_i)

        max_profit = 0
        while job_chain_heap:
            _, chained_profit = heapq.heappop(job_chain_heap)
            max_profit = max(max_profit, chained_profit)
        return max_profit

    def jobScheduling(self, startTimes: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []

        for i in range(len(profit)):
            job = (startTimes[i], endTime[i], profit[i])
            jobs.append(job)

        jobs.sort()

        for i in range(len(profit)):
            startTimes[i], _, _ = jobs[i]

        return self._findMaxProfit(jobs)


if __name__ == "__main__":
    sol = SolutionDP()
    a = sol.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70])
    print(a)
    sol2 = SolutionPriorityQueue()
    b = sol2.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70])
    print(b)
