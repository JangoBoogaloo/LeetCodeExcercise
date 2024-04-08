from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k < 1:
            return 0
        product = 1
        count, left, right = 0, 0, 0
        while right < len(nums):
            data = nums[right]
            right += 1
            product *= data
            while product >= k and right > left:
                product //= nums[left]
                left += 1
            count += right - left
        return count


if __name__ == "__main__":
    solution = Solution()
    ans = solution.numSubarrayProductLessThanK([10,5,2,6], 100)
    print(ans)