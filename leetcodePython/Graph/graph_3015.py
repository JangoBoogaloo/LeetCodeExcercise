from typing import List


class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        housePairForStreets = [0] * n
        for house1 in range(1, n+1):
            for house2 in range(house1+1, n+1):
                h1_h2 = house2 - house1
                h1_x_y_h2 = abs(house1 - x) + 1 + abs(house2 - y)
                h1_y_x_h2 = abs(house1 - y) + 1 + abs(house2 - x)
                streets = min(h1_x_y_h2, h1_y_x_h2, h1_h2)
                housePairForStreets[streets - 1] += 2
        return housePairForStreets







