from typing import List


class SolutionDP:
    def getMaxLen(self, nums: List[int]) -> int:
        size = len(nums)
        pos_max_end_at = [0] * size
        neg_max_end_at = [0] * size
        if nums[0] > 0: pos_max_end_at[0] = 1
        elif nums[0] < 0: neg_max_end_at[0] = 1

        ans = pos_max_end_at[0]

        for i in range(1, size):
            if nums[i] > 0:
                pos_max_end_at[i] = 1 + pos_max_end_at[i - 1]
                if neg_max_end_at[i - 1] > 0:
                    neg_max_end_at[i] = 1 + neg_max_end_at[i - 1]
                else:
                    neg_max_end_at[i] = 0
            elif nums[i] < 0:
                if neg_max_end_at[i - 1] > 0:
                    pos_max_end_at[i] = 1 + neg_max_end_at[i - 1]
                else:
                    pos_max_end_at[i] = 0
                neg_max_end_at[i] = 1 + pos_max_end_at[i - 1]
            ans = max(ans, pos_max_end_at[i])
        return ans


if __name__ == "__main__":
    sol = Solution()
    sol.getMaxLen([0,1,-2,-3,-4])