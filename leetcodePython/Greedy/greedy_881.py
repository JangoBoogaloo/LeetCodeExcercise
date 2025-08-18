class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        small, big = 0, len(people) -1
        boats = 0
        while small <= big:
            boats += 1
            if people[small] + people[big] <= limit:
                small += 1
            big -= 1
        return boats
