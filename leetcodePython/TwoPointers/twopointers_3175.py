from typing import List


class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        prevWinIndex, newIndex = 0, 1
        maxWin = 0
        while newIndex < len(skills):
            if skills[prevWinIndex] < skills[newIndex]:
                maxWin = 1
                prevWinIndex = newIndex
            else:
                 maxWin += 1
            if maxWin == k:
                break
            newIndex += 1
        return prevWinIndex