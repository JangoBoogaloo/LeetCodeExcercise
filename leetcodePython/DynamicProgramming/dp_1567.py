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


class SolutionOptimize:
    def getMaxLen(self, nums: List[int]) -> int:
        size = len(nums)
        positive_array_length = 0
        negative_array_length = 0
        if nums[0] > 0:
            positive_array_length = 1
        elif nums[0] < 0:
            negative_array_length = 1

        ans = positive_array_length

        for i in range(1, size):
            if nums[i] > 0:
                positive_array_length += 1
                if negative_array_length > 0:
                    negative_array_length += 1
            elif nums[i] < 0:
                if negative_array_length > 0:
                    positive_array_length, negative_array_length = negative_array_length, positive_array_length
                    positive_array_length += 1
                    negative_array_length += 1
                else:
                    negative_array_length = 1 + positive_array_length
                    positive_array_length = 0
            else:  # nums[i] == 0
                positive_array_length, negative_array_length = 0, 0
            ans = max(ans, positive_array_length)
        return ans