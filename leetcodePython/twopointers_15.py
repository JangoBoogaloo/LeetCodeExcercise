from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            # this check is to avoid duplicate
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, result)
        return result

    def twoSum(self, nums: List[int], i: int, result: List[List[int]]):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            threesum = nums[i] + nums[left] + nums[right]
            if threesum < 0:
                left += 1
            elif threesum > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1


if __name__ == '__main__':
    solution = Solution()
    result = solution.threeSum([-1,0,1,2,-1,-4])
    print(result)
