from typing import List


class SolutionBS:
    def maxJump(self, stones: List[int]) -> int:
        l, r = 0, stones[-1]
        while l <= r:
            m = (l + r) // 2
            if self._check(stones, m):
                r = m - 1
            else:
                l = m + 1
        return l

    def _check(self, stones, maxJump):
        length = len(stones)
        used = [False] * length  # track if the stone has been jumped over or not
        lastUsedPos = 0  # the last stone we jumped
        # we jump as far as possible until reach last stone
        for i in range(length):
            # if the distance between next stone(stones[i]) and the last stone we jumped > max jumping length,
            # we jump to the stone before next stone(stones[i-1])
            # the stone before next stone(stones[i-1]) is the last stone we jumped, return False.
            # we can not cross the river
            if stones[i] - stones[lastUsedPos] > maxJump:
                if i - 1 == lastUsedPos: return False
                lastUsedPos = i - 1
                used[lastUsedPos] = True
        used[length - 1] = True
        lastUsedPos = length - 1
        # we just jump to the stone we didn't jump over in order
        for i in range(length - 1, -1, -1):
            # if the stone(stones[i]) we didn't jump, we jump to it,
            # and check if the distance between the stone(stones[i]) and the last stone we jumped > max jumping length or not.
            if not used[i]:
                if stones[lastUsedPos] - stones[i] > maxJump: return False
                lastUsedPos = i
        return True


class SolutionGreedy:
    def maxJump(self, stones: List[int]) -> int:
        distance = stones[1] - stones[0]
        for i in range(2, len(stones)):
            distance = max(distance, stones[i] - stones[i-2])
        return distance