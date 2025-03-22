from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            isLeftEmpty = (i == 0) or flowerbed[i-1] == 0
            isRightEmpty = (i==len(flowerbed)-1) or flowerbed[i+1] == 0
            if isLeftEmpty and isRightEmpty:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return n == 0
