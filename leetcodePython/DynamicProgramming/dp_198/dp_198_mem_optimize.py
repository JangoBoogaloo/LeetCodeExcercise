from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxGain2HouseBefore = 0
        maxGain1HouseBefore = nums[0]
        currMaxGain = maxGain1HouseBefore
        for currHouse in range(1, len(nums)):
            robCurrentOption = nums[currHouse] + maxGain2HouseBefore
            skipCurrentOption = maxGain1HouseBefore
            currMaxGain = max(robCurrentOption, skipCurrentOption)
            maxGain1HouseBefore, maxGain2HouseBefore = currMaxGain, maxGain1HouseBefore
        return currMaxGain





