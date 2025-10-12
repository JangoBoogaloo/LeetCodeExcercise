from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique = set()
        for num in nums:
            if num in unique:
                return num
            else:
                unique.add(num)
        raise Exception(f"{nums} does not contain duplicate data")
