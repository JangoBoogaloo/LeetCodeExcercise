class Solution:
    def bestClosingTime(self, customers: str) -> int:
        earliest = penalty = min_penalty = 0
        for close, c in enumerate(customers):
            if c == "Y":
                penalty -= 1
            else:
                penalty += 1
            if penalty < min_penalty:
                earliest = close + 1
                min_penalty = penalty
        return earliest
