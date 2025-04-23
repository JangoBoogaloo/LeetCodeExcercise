import collections
from typing import List
from heapq import heappush, heappop

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        id_top5 = collections.defaultdict(list)
        for student_id, score in items:
            heappush(id_top5[student_id], score)
            if len(id_top5[student_id]) > 5:
                heappop(id_top5[student_id])
        return sorted([[student_id, sum(id_top5[student_id]) // 5] for student_id in id_top5])
