from typing import List
from heapq import *


class Solution:
    def _get_place(self, place: int) -> str:
        match place:
            case 1:
                return "Gold Medal"
            case 2:
                return "Silver Medal"
            case 3:
                return "Bronze Medal"
            case _:
                return f"{place}"

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_heap = [[-score, i] for i, score in enumerate(score)]
        heapify(score_heap)
        ans = [""] * len(score)
        place = 1
        while score_heap:
            index = heappop(score_heap)[1]
            ans[index] = self._get_place(place)
            place += 1
        return ans
