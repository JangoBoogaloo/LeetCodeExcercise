from typing import List


class SolutionCountSort:
    def sortColors(self, nums: List[int]) -> None:
        count_0, count_1, count_2 = 0, 0, 0
        for num in nums:
            if num == 0:
                count_0 += 1
            elif num == 1:
                count_1 += 1
            else:
                count_2 += 1
        for i in range(len(nums)):
            if count_0 > 0:
                nums[i] = 0
                count_0 -= 1
            elif count_1 > 0:
                nums[i] = 1
                count_1 -= 1
            else:
                nums[i] = 2


class SolutionDutchNationalFlag:
    def sortColors(self, nums: List[int]) -> None:
        i1, i2, i3 = 0, 0, len(nums) - 1
        num1, num2, num3 = 0, 1, 2
        while i2 <= i3:
            if nums[i2] == num1:
                nums[i1], nums[i2] = nums[i2], nums[i1]
                i1 += 1
                i2 += 1
            elif nums[i2] == num2:
                i2 += 1
            else:  # nums[i2] == num3
                nums[i2], nums[i3] = nums[i3], nums[i2]
                i3 -= 1
