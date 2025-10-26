#pseudo, to pass interpretation only
def knows(a: int, b: int) -> bool:
    return True

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for people in range(1, n):
            if knows(candidate, people) or not knows(people, candidate):
                candidate = people

        for people in range(n):
            if candidate == people:
                continue
            if knows(candidate, people) or not knows(people, candidate):
                return -1
        return candidate




