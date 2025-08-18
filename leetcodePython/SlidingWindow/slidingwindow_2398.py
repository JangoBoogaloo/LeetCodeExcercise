from collections import deque
from typing import List


class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        time_decrease_index = deque()
        left = 0
        running_cost_sum = 0
        for right in range(len(chargeTimes)):
            while time_decrease_index and chargeTimes[right] >= chargeTimes[time_decrease_index[-1]]:
                time_decrease_index.pop()
            time_decrease_index.append(right)
            running_cost_sum += runningCosts[right]
            max_charge_time = chargeTimes[time_decrease_index[0]]
            cost = max_charge_time + (right - left + 1) * running_cost_sum
            if cost > budget:
                if time_decrease_index[0] == left:
                    time_decrease_index.popleft()
                running_cost_sum -= runningCosts[left]
                left += 1
        return len(chargeTimes) - left








