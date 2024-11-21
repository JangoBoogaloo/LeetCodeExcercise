class Solution:
    def bestClosingTime(self, customers: str) -> int:
        close = penalty = min_penalty = 0
        CUSTOMER_ENTER = "Y"
        for open_i, ch in enumerate(customers):
            if ch == CUSTOMER_ENTER:
                penalty -= 1
            else:  # ch == NO_CUSTOMER
                penalty += 1
            if penalty < min_penalty:
                close = open_i + 1
                min_penalty = penalty
        return close
