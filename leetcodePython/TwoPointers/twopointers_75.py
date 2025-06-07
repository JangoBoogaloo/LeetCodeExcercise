from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        indexZero = 0
        indexTwo = len(nums) - 1
        currentIndex = 0
        while currentIndex <= indexTwo:
            if nums[currentIndex] == 0:
                nums[indexZero], nums[currentIndex] = nums[currentIndex], nums[indexZero]
                indexZero += 1
                currentIndex += 1
            elif nums[currentIndex] == 2:
                nums[indexTwo], nums[currentIndex] = nums[currentIndex], nums[indexTwo]
                indexTwo -= 1
            else:
                currentIndex += 1





