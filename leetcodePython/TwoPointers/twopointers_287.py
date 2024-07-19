from typing import List


class SolutionSort:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]


class SolutionSet:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)


class SolutionCycleDetection:
    def findDuplicate(self, nums: List[int]) -> int:
        # [2, 2, 1]  a[0]->a[2]->a[1]->a[2]
        # for a link list solution base on value->index of value approach
        # now we get circular list

        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow