import collections
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # data in fruits array represent fruit type, consider it as a fruit type id

        # we only have 2 basket, can only hold two types
        # which means within the capture, we can only see 2 different fruit id

        # we want the biggest window such that have only 2 Ids

        window_fruit_types = {}
        left = 0
        max_picked = 0
        for right, fruit_type in enumerate(fruits):

            if fruit_type not in window_fruit_types:
                window_fruit_types[fruit_type] = 0
            window_fruit_types[fruit_type] += 1
            if len(window_fruit_types) > 2:
                old_fruit_type = fruits[left]
                window_fruit_types[old_fruit_type] -= 1
                if window_fruit_types[old_fruit_type] == 0:
                    del window_fruit_types[old_fruit_type]
                left += 1
        return right - left + 1