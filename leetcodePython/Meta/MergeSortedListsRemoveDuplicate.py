from typing import List


class Solution:
    def mergeSortedListsRemoveDuplicate(self, lists: List[List[int]]) -> List[int]:
        distinct = set()
        for li in lists:
            for data in li:
                distinct.add(data)
        return sorted(distinct)






import pytest
target = Solution()

@pytest.mark.parametrize("lists, expect",
[
    ([[1, 2, 3], [1, 2, 3], [1, 2, 3]], [1, 2, 3]),
    ([[1, 2, 3], [4, 4, 4], [5, 6, 7]], [1, 2, 3, 4, 5, 6, 7]),
    ([[1, 4, 4], [2, 3, 5], [4, 6, 7, 7, 7, 7, 7, 7]], [1, 2, 3, 4, 5, 6, 7]),

])
def test_mergeSortedListsRemoveDuplicate(lists: List[List[int]], expect:List[int]):
    assert target.mergeSortedListsRemoveDuplicate(lists) == expect
