from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        window_size = 2 * k + 1
        if len(nums) < window_size:
            return [-1] * len(nums)
        averages = [-1] * k
        curr_sum = sum(nums[0:window_size])
        averages.append(curr_sum//window_size)
        for i in range(k+1, len(nums)-k):
            curr_sum += nums[i+k] - nums[i-k-1]
            averages.append(curr_sum//window_size)
        averages.extend([-1]*k)
        return averages


if __name__ == "__main__":
    sol = Solution()
    avg = sol.getAverages([8], 3)
    print(avg)