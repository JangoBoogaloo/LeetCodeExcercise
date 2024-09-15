from typing import List


class Solution:
    def _enough_operation(self, nums: List[int], x: int, y: int, steps: int) -> bool:
        count_x = steps
        for num in nums:
            # 8 / 2 = 4
            # 7 / 2 = 3  we want 4
            # (8 + 2 -1) / 2 = 4
            # (7 + 2 - 1) / 2 = 4
            require_y_ops = (num + y - 1) // y
            if steps < require_y_ops:
                num_after_y_ops = num - steps * y
                require_x_ops = (num_after_y_ops + x - 1) // x
                count_x -= require_x_ops
                if count_x < 0:
                    return False
        return True

    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        left, right = 0, max(nums)
        # make x remain subtract after y subtract so x operation includes y
        x -= y
        while left <= right:
            guess_ops = (left + right) // 2
            if self._enough_operation(nums, x, y, guess_ops):
                right = guess_ops - 1
            else:
                left = guess_ops + 1
        return right + 1
