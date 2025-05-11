from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_len = len(cardPoints) - k
        left = remain_points = total_point = 0

        for point in cardPoints:
            total_point += point
        min_remain_point = total_point
        if window_len == 0:
            return total_point
        for right, point in enumerate(cardPoints):
            remain_points += point
            if right - left + 1 == window_len:
                min_remain_point = min(min_remain_point, remain_points)
                remain_points -= cardPoints[left]
                left += 1

        return total_point - min_remain_point

