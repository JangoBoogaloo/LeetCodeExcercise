from typing import List
from union_find import UF

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf = UF()
        [uf.add(i) for i in range(n)]
        answer = []
        for a, b in requests:
            componentA, componentB = uf.find(a), uf.find(b)
            for c, d in restrictions:
                componentC, componentD = uf.find(c), uf.find(d)
                if (componentA == componentC and componentB == componentD) or (componentA == componentD and componentB == componentC):
                    answer.append(False)
                    break
            else:
                answer.append(True)
                uf.union(componentA, componentB)
        return answer








