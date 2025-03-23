from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        start = 0
        current =0
        for i in range(len(gas)):
            balance = gas[i] - cost[i]
            total += balance
            current += balance
            if current < 0:
                current = 0
                start = i + 1
        return start if total >= 0 else -1