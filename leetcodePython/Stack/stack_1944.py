from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        answer = [0] * len(heights)
        decreaseHeightIndex = []
        for i in range(len(heights)):
            while decreaseHeightIndex and heights[i] >= heights[decreaseHeightIndex[-1]]:
                answer[decreaseHeightIndex[-1]] += 1
                decreaseHeightIndex.pop()
            # latest height remain in stack is higher than current height
            if decreaseHeightIndex:
                answer[decreaseHeightIndex[-1]] += 1

            decreaseHeightIndex.append(i)
        return answer


class VisibleIndex:
    def canSeePersons(self, heights: List[int]) -> List[List[int]]:
        answer: List[List[int]]
        answer = [[] for _ in range(len(heights))]
        decreaseHeightIndex = []
        for i in range(len(heights)):
            while decreaseHeightIndex and heights[i] >= heights[decreaseHeightIndex[-1]]:
                answer[decreaseHeightIndex[-1]].append(i)
                decreaseHeightIndex.pop()

            # latest height remain in stack is higher than current height
            if decreaseHeightIndex:
                answer[decreaseHeightIndex[-1]].append(i)

            decreaseHeightIndex.append(i)
        return answer


if __name__ == '__main__':
    solution = VisibleIndex()
    print(solution.canSeePersons([4,5,6]))