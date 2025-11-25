from typing import List


class Solution:
    @staticmethod
    def _addProductSegment(answer, product):
        if answer and answer[-1][0] == product[0]:
            answer[-1][1] += product[1]
        else:
            answer.append(product)

    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i1 = i2 = 0
        answer = []
        while i1 < len(encoded1) or i2 < len(encoded2):
            num1, count1 = encoded1[i1]
            num2, count2 = encoded2[i2]
            if count1 < count2:
                productSegment = [num1*num2, count1]
                encoded2[i2][1] = count2 - count1
                self._addProductSegment(answer, productSegment)
                i1 += 1
            elif count2 < count1:
                productSegment = [num1*num2, count2]
                encoded1[i1][1] = count1 - count2
                self._addProductSegment(answer, productSegment)
                i2 += 1
            else:
                productSegment = [num1*num2, count2]
                self._addProductSegment(answer, productSegment)
                i1 += 1
                i2 += 1
        return answer








import pytest
target = Solution()

@pytest.mark.parametrize("encode1, encode2, expect",
[
    ([[1, 2], [2, 1], [3, 2]], [[6, 2], [3, 2], [2, 1]], [[6, 3], [9, 1], [6, 1]]),
])
def test_findRLEArray(encode1, encode2, expect):
    assert target.findRLEArray(encode1, encode2) == expect
