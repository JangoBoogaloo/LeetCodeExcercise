from collections import Counter
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    @staticmethod
    def _pushBackRemain(negFreq: int, ch: str, pq: List[tuple[int, str]]):
        if negFreq + 1 != 0:
            heappush(pq, (negFreq+1, ch))

    def reorganizeString(self, s: str) -> str:
        ans = []
        txtFreq = Counter(s)
        pq = [(-count, char) for char, count in txtFreq.items()]
        heapify(pq)
        while pq:
            currCount, currCh = heappop(pq)
            if not ans or currCh != ans[-1]:
                ans.append(currCh)
                self._pushBackRemain(currCount, currCh, pq)
            elif not pq:
                return ""
            else:
                nextCount, nextCh = heappop(pq)
                ans.append(nextCh)
                self._pushBackRemain(nextCount, nextCh, pq)
                heappush(pq, (currCount, currCh))
        return "".join(ans)

