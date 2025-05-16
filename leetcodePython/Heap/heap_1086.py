import collections
from typing import List
from heapq import *

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        id_scores = collections.defaultdict(list)

        for id, score in items:
            heappush(id_scores[id], score)
            if len(id_scores[id]) > 5:
                heappop(id_scores[id])
        res = [[id, sum(id_scores[id]) // len(id_scores[id])] for id in sorted(id_scores)]
        return res