from typing import List


class SolutionBruteForce:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        pairs = 0
        for j in range(1, len(nums1)):
            for i in range(j):
                if (nums1[i] + nums1[j]) > (nums2[i] + nums2[j]):
                    pairs += 1
        return pairs


class SolutionBS:
    @staticmethod
    def _positive_sum_j_from_i(diff: List[int], i: int) -> int:
        # diff[i] + diff[j] > 0
        left = i + 1
        right = len(diff) - 1
        while left <= right:
            guess_j = (left + right) // 2
            if diff[i] + diff[guess_j] <= 0:
                left = guess_j + 1
            else:
                right = guess_j - 1
        return left

    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1[i] - nums2[i] + nums1[j] - nums2[j] > 0
        diff = [nums1[i] - nums2[i] for i in range(len(nums1))]
        diff.sort()
        pairs = 0
        for i in range(len(diff)):
            if diff[i] > 0:
                j = i + 1
            else:
                j = self._positive_sum_j_from_i(diff, i)
            pairs += len(diff) - j
        return pairs


class SolutionTwoPointers:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1[i] - nums2[i] + nums1[j] - nums2[j] > 0
        # diff[i] + diff[j] > 0
        diff = [nums1[i] - nums2[i] for i in range(len(nums1))]
        diff.sort()
        pairs = 0
        left_i, right_j = 0, len(nums1) - 1
        while left_i < right_j:
            if diff[left_i] + diff[right_j] > 0:
                # pairs with j bigger than right_j
                pairs_j = right_j - left_i
                pairs += pairs_j
                right_j -= 1
            else:
                left_i += 1
        return pairs


if __name__ == "__main__":
    sol = SolutionBS()
    ans = sol.countPairs([2, 1, 2, 1], [1, 2, 1, 2])
    print(ans)
    ans = sol.countPairs([1, 10, 6, 2], [1, 4, 1, 5])
    print(ans)
