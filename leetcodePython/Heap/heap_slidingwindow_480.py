from collections import defaultdict
from typing import List
from heapq import heappush, heappop


class Solution:
    def _get_median(self, small_half, big_half, heap_size: int):
        if heap_size % 2 == 1:
            return -small_half[0]
        else:
            return (-small_half[0] + big_half[0]) / 2

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small_half, big_half = [], []
        remove_num_freq = defaultdict(int)
        result = []
        # 1st k element
        for i in range(k):
            heappush(small_half, -nums[i])
            heappush(big_half, -heappop(small_half))
            if len(small_half) < len(big_half):
                heappush(small_half, -heappop(big_half))

        median = self._get_median(small_half, big_half, k)
        result.append(median)

        for right in range(k, len(nums)):
            remove_num = nums[right - k]
            add_num = nums[right]
            remove_num_freq[remove_num] += 1

            if remove_num > median:
                # the remove number is supposed to remove from big half, small have 1 element more than big
                small_more_than_big = 1
            else:
                small_more_than_big = -1

            if add_num <= median:
                # the add number is supposed to add to small half, small have 1 element more than big
                small_more_than_big += 1
                heappush(small_half, -add_num)
            else:
                small_more_than_big -= 1
                heappush(big_half, add_num)

            # small have less than big
            if small_more_than_big < 0:
                # move from big to small
                heappush(small_half, -heappop(big_half))
            # small have more than big
            elif small_more_than_big > 0:
                # move from small to big
                heappush(big_half, -heappop(small_half))

            # at this stage heap is already balanced, just remove the data that marked as removed

            while small_half and remove_num_freq[-small_half[0]] > 0:
                remove_num_freq[-small_half[0]] -= 1
                heappop(small_half)

            while big_half and remove_num_freq[big_half[0]] > 0:
                remove_num_freq[big_half[0]] -= 1
                heappop(big_half)

            median = self._get_median(small_half, big_half, k)
            result.append(median)

        return result


from sortedcontainers import SortedList


class SolutionSortedList:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        sortedList = SortedList()
        res = []
        for i in range(len(nums)):
            sortedList.add(nums[i])
            if len(sortedList) > k:
                sortedList.remove(nums[i - k])
            if len(sortedList) == k:
                if k % 2 == 1:
                    median = sortedList[k // 2]
                else:
                    median = (sortedList[k // 2 - 1] + sortedList[k // 2]) / 2
                res.append(median)
        return res


if __name__ == "__main__":
    sol = Solution()
    ans = sol.medianSlidingWindow([1, 2, 3, 4, 5, 6, 7], 3)
    print(ans)
