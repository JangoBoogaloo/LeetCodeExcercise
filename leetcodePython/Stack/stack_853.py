from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionAndSpeed = sorted(zip(position, speed))
        positionSortedTimeStack = []
        for pos, speed in positionAndSpeed:
            positionSortedTimeStack.append(float(target - pos) / speed)

        fleets = 0
        while len(positionSortedTimeStack) > 1:
            leadTime = positionSortedTimeStack.pop()
            if leadTime < positionSortedTimeStack[-1]:
                fleets += 1
            else:
                positionSortedTimeStack[-1] = leadTime
        return fleets + bool(positionSortedTimeStack)
