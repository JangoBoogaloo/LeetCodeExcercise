from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # within that x minutes, we want to get the maximum of customers, and that owner is grumpy

        # we calculate total customer
        # we base on grumpy to calculate unhappy customers in every minute, store in array, calculate total unhappy
        # we slide window, get a window such that the unhappy customer is maximum = reduced_unhappy
        # total customer - (unhappy customers - reduced_unhappy

        total_customers = sum(customers)
        for i in range(len(customers)):
            customers[i] = customers[i]*grumpy[i]
        bad_list = customers
        total_unsatisfied = sum(bad_list)
        bad_in_window = 0
        max_bad = sum(bad_list[:minutes])
        left = 0
        for right, new_bad in enumerate(bad_list):
            bad_in_window += new_bad
            if right - left == minutes:
                bad_in_window -= bad_list[left]
                max_bad = max(max_bad, bad_in_window)
                left += 1
        return total_customers - total_unsatisfied + max_bad
