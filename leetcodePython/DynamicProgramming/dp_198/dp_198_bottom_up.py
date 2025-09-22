from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        maxGainWithHouseCount = [0] * (len(nums) + 1)
        maxGainWithHouseCount[1] = nums[0]
        for houseCount in range(2, len(nums) + 1):
            index = houseCount - 1
            robCurrent = nums[index] + maxGainWithHouseCount[houseCount - 2]
            skipCurrent = maxGainWithHouseCount[houseCount - 1]
            maxGainWithHouseCount[houseCount] = max(robCurrent, skipCurrent)
        return maxGainWithHouseCount[len(nums)]





