class SolutionIterative:
    def findPeakElement(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1


class SolutionBS:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # from this num to right, unlikely to get a peak
            if nums[mid] > nums[mid + 1]:
                right = mid
            # this number is smaller than next number, then pick should be at it's right
            else:
                left = mid + 1
        return left
