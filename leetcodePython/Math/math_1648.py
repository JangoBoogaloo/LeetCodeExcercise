from collections import Counter
from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        sortedInventory = sorted(Counter(inventory).items(), reverse=True)
        sortedInventory.append((0,0))
        ans, index, width = 0, 0, 0

        while orders > 0:
            width += sortedInventory[index][1]
            sell = min(orders, width * (sortedInventory[index][0] - sortedInventory[index + 1][0]))
            whole, remainder = divmod(sell, width)
            ans += width * (whole * (sortedInventory[index][0] + sortedInventory[index][0] - (whole - 1))) // 2 + remainder * (sortedInventory[index][0] - whole)
            orders -= sell
            index += 1
        return ans % 1_000_000_007