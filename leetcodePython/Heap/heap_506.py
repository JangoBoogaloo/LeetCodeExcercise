from typing import List


class Solution:
    _RANK = ["Gold Medal", "Silver Medal", "Bronze Medal"]

    @staticmethod
    def _getRank(rank: int) -> str:
        if rank < len(Solution._RANK):
            return Solution._RANK[rank]
        return f"{rank+1}"

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_index = [(-s, i) for i, s in enumerate(score)]
        score_index.sort()
        answer = [""] * len(score)
        for rank, (_, index) in enumerate(score_index):
            answer[index] = self._getRank(rank)
        return answer
