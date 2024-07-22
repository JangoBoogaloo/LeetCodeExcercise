from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        small_i = 0
        big_j = len(people) - 1
        left_people = len(people)
        boat = 0

        while small_i < big_j:
            if people[small_i] + people[big_j] > limit:
                big_j -= 1
                continue
            left_people -= 2
            boat += 1
            small_i += 1
            big_j -= 1
        return boat + left_people
