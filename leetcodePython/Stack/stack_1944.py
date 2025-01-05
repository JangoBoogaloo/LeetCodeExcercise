from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        answer = [0] * len(heights)
        decreaseHeightIndex = []
        for i in range(len(heights)):
            while decreaseHeightIndex and heights[i] >= heights[decreaseHeightIndex[-1]]:
                answer[decreaseHeightIndex[-1]] += 1
                decreaseHeightIndex.pop()

            if decreaseHeightIndex:
                answer[decreaseHeightIndex[-1]] += 1

            decreaseHeightIndex.append(i)
        return answer
