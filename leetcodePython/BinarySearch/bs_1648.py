import heapq
from typing import List


class Solution:
    def arithmeticSum(self, a_n: int, a_1: int, n: int) -> int:
        return (a_n + a_1 + 1) * n // 2

    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True) # inventory high to low
        inventory += [0]
        ans = 0
        greater_element_count = 1
        for i in range(len(inventory)-1):
            if inventory[i] > inventory[i+1]:
                n = inventory[i] - inventory[i+1]
                if greater_element_count*n < orders:
                    ans += greater_element_count * self.arithmeticSum(inventory[i], inventory[i+1], n)
                    orders -= greater_element_count*n
                else:
                    q, r = divmod(orders, greater_element_count)
                    magic = greater_element_count*(2*inventory[i] - q + 1) * q//2 + r*(inventory[i] - q)
                    ans += magic
                    return ans % 1_000_000_007
            greater_element_count += 1