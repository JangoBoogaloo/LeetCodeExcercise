import collections
from typing import List


class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        robots, max_time, cost_sum = 0, 0, 0
        size = len(chargeTimes)
        left = 0
        dq_decrease = collections.deque()

        for right in range(size):
            cost_sum += runningCosts[right]
            while dq_decrease and chargeTimes[dq_decrease[-1]] <= chargeTimes[right]:
                dq_decrease.pop()
            dq_decrease.append(right)
            max_time = chargeTimes[dq_decrease[0]]
            cost_formula = max_time + (right - left + 1) * cost_sum
            if cost_formula > budget:
                if dq_decrease[0] == left:
                    dq_decrease.popleft()
                cost_sum -= runningCosts[left]
                left += 1
        return size - left
