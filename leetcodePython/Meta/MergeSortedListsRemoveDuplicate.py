from typing import List


class Solution:
    def mergeSortedListsRemoveDuplicate(self, lists: List[List[int]]) -> List[int]:
        distinct = set()
        for li in lists:
            for data in li:
                distinct.add(data)
        return sorted(distinct)





