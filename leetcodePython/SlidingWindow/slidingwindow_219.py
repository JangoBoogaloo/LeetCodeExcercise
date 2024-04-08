from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        distinct = set()
        for i in range(len(nums)):
            if nums[i] in distinct:
                return True
            distinct.add(nums[i])
            if len(distinct) > k:
                distinct.remove(nums[i-k])
        return False