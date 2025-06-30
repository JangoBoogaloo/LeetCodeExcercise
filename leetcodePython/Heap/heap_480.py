from typing import List
from median_finder import MedianFinder

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medianFinder = MedianFinder()
        for num in nums[:k]:
            medianFinder.add(num)
        medians = [medianFinder.median()]
        for i in range(k, len(nums)):
            medianFinder.add(nums[i])
            medianFinder.remove(nums[i-k])
            medians.append(medianFinder.median())
        return medians
