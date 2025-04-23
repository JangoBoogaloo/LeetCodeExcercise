from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        increasePriceIndexStack = []
        for i in range(len(prices)):
            while increasePriceIndexStack and prices[i] <= prices[increasePriceIndexStack[-1]]:
                biggerPriceIndex = increasePriceIndexStack.pop()
                prices[biggerPriceIndex] -= prices[i]
            increasePriceIndexStack.append(i)
        return prices
