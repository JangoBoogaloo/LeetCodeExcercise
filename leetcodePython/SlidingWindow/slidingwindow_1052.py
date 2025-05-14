from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_customers = sum(customers)
        unsatisfied_list = [customers[i]*grumpy[i] for i in range(len(customers))]
        total_unsatisfied = sum(unsatisfied_list)
        curr_unsatisfied = sum(unsatisfied_list[:minutes])
        max_unsatisfied = curr_unsatisfied
        for right in range(minutes, len(unsatisfied_list)):
            curr_unsatisfied += unsatisfied_list[right] - unsatisfied_list[right-minutes]
            max_unsatisfied = max(max_unsatisfied, curr_unsatisfied)
        return total_customers - total_unsatisfied + max_unsatisfied
