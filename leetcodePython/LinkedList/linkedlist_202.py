class Solution:
    @staticmethod
    def _next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit**2
        return total_sum

    def isHappy(self, n: int) -> bool:
        slow, fast = n, self._next(n)
        while fast != 1 and slow != fast:
            slow = self._next(slow)
            fast = self._next(self._next(fast))
        return fast == 1