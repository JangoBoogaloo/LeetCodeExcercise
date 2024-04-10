from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0
        min_index = max_index = left = -1
        for right in range(len(nums)):
            if nums[right] < minK or nums[right] > maxK:
                left = right
            if nums[right] == minK:
                min_index = right
            if nums[right] == maxK:
                max_index = right

            '''
            We expect the relation like this
            .....left......index1.....index2....right
            
            the `left` is out of bound
            from left to index1 are all combinations of inbound arrays
            '''
            index1 = min(min_index, max_index)
            answer += max(0, index1-left)
        return answer
