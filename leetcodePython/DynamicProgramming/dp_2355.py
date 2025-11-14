from typing import List


class Solution:
    def _maxBooksBtw(self, left: int, right: int, books: List[int]) -> int:
        rightHeight = books[right]
        distance = min(books[right], right - left + 1)
        leftHeight = books[right] - (distance - 1)
        return (leftHeight + rightHeight) * distance // 2

    def maximumBooks(self, books: List[int]) -> int:
        increaseSlopeIndex = []
        takeBooksAt = [0] * len(books)
        for right in range(len(books)):
            while increaseSlopeIndex:
                left = increaseSlopeIndex[-1]
                if books[right] - books[left] <= right - left:
                    increaseSlopeIndex.pop()
                else:
                    break
            if increaseSlopeIndex:
                left = increaseSlopeIndex[-1]
                takeBooksAt[right] = takeBooksAt[left] + self._maxBooksBtw(left + 1, right, books)
            else:
                takeBooksAt[right] = self._maxBooksBtw(0, right, books)
            increaseSlopeIndex.append(right)
        return max(takeBooksAt)










import pytest
target = Solution()


@pytest.mark.parametrize("books, expect",
[
    ([1, 2, 3], 1+2+3),
    ([1, 2, 2], 0+1+2),
    ([1, 2, 3, 5, 6], 6+11),
    ([1, 2, 3, 1, 5, 6], 0 + 1 + 5 + 6),

])
def test_maximumBooks(books, expect):
    assert target.maximumBooks(books) == expect