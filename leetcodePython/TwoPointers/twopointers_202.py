class Solution:
    def isHappy(self, n: int) -> bool:
        def next(num: int) -> int:
            next_num = 0
            while num != 0:
                digit = num % 10
                next_num += digit * digit
                num = num // 10
            return next_num

        slow = n
        fast = next(n)
        if fast == 1:
            return True
        while slow != fast:
            slow = next(slow)
            fast = next(next(fast))
            if fast == 1:
                return True
        return False
