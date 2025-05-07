from typing import List


class Solution:
    def mergeSortedListsRemoveDuplicate(self, lists: List[List[int]]) -> List[int]:
        distinct = set()
        for li in lists:
            for data in li:
                distinct.add(data)
        return sorted(distinct)


if __name__ == "__main__":
    sol = Solution()
    result = sol.mergeSortedListsRemoveDuplicate([[1,1,1,1,1,2,3],[2,2,2,2,2,3,4]])
    print(result)