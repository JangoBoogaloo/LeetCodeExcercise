from typing import List


class SolutionReverse:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        # [0,1,2], k= 1

        # [2,1,0]
        nums.reverse()
        def partial_reverse(full_nums, start, end):
            while start < end:
                full_nums[start], full_nums[end] = full_nums[end], full_nums[start]
                start += 1
                end -= 1

        # [2, 1, 0]
        partial_reverse(nums, 0, k-1)

        # [2, 0, 1]
        partial_reverse(nums, k, len(nums)-1)


class SolutionCyclicReplacement:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        start_i = count = 0
        while count < n:
            current_i = start_i
            prev_num = nums[start_i]
            while True:
                next_i = (current_i + k) % n
                nums[next_i], prev_num = prev_num, nums[next_i]
                current_i = next_i
                count += 1
                if start_i == current_i:
                    break
            start_i += 1
