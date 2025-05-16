from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        # Min heap ordered by character counts, so we will use
        # negative values for count
        pq = [(-count, char) for char, count in Counter(s).items()]
        heapify(pq)
        while pq:
            count, ch = heappop(pq)
            if not ans or ch != ans[-1]:
                ans.append(ch)
                if count + 1 != 0:
                    heappush(pq, (count + 1, ch))
            else:
                if not pq:
                    return ""
                count_2, ch_2 = heappop(pq)
                ans.append(ch_2)
                if count_2 + 1 != 0:
                    heappush(pq, (count_2 + 1, ch_2))
                heappush(pq, (count, ch))
        return "".join(ans)


if __name__ == "__main__":
    sol = Solution()
    print(sol.reorganizeString("aaaabc"))
