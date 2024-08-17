from typing import List


class SolutionBSPrefixSum:
    @staticmethod
    def _piece_with_sweetness(sweet_prefix_sum: List[int], sweetness: int) -> int:
        piece = 1
        if len(sweet_prefix_sum) < 2:
            return piece
        r = len(sweet_prefix_sum) - 1
        for l in range(len(sweet_prefix_sum) - 2, -1, -1):
            piece_sweet = sweet_prefix_sum[r] - sweet_prefix_sum[l]
            if piece_sweet >= sweetness and sweet_prefix_sum[l] >= sweetness:
                r = l
                piece += 1
        return piece

    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        prefix_sum = []
        sweet_sum = 0
        for sweet in sweetness:
            sweet_sum += sweet
            prefix_sum.append(sweet_sum)

        left = min(sweetness)
        right = prefix_sum[-1]
        while left < right:
            guess_sweetness = (left + right + 1) // 2
            if self._piece_with_sweetness(prefix_sum, guess_sweetness) < k + 1:
                right = guess_sweetness - 1
            else:
                left = guess_sweetness
        return left


class SolutionBS:
    @staticmethod
    def _piece_with_sweetness(sweetness: List[int], sweet: int) -> int:
        piece = 0
        curr_sweet = 0
        for s in sweetness:
            curr_sweet += s
            if curr_sweet >= sweet:
                piece += 1
                curr_sweet = 0
        return piece

    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        prefix_sum = []
        sweet_sum = 0
        for sweet in sweetness:
            sweet_sum += sweet
            prefix_sum.append(sweet_sum)

        left = min(sweetness)
        right = sum(sweetness) // (k + 1)
        while left < right:
            guess_sweetness = (left + right + 1) // 2
            if self._piece_with_sweetness(sweetness, guess_sweetness) < k+1:
                right = guess_sweetness - 1
            else:
                left = guess_sweetness
        return right
