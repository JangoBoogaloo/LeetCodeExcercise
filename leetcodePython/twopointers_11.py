from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left_p = 0
        right_p = len(height) - 1
        while left_p < right_p:
            width = right_p - left_p
            min_height = min(height[left_p], height[right_p])
            area = width * min_height
            max_area = max(max_area, area)
            if height[left_p] < height[right_p]:
                left_p += 1
            else:
                right_p -= 1
        return max_area

if __name__ == '__main__':
    solution = Solution()
    solution.maxArea([1,8,6,2,5,4,8,3,7])