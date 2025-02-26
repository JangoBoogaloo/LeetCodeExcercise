class Solution:
    def _nextGreaterElement(self, n: str) -> str:
        # 234157641
        digits = list(n)
        no_increase = len(digits) - 1

        # 2341 5 7641
        while no_increase - 1 >= 0 and digits[no_increase] <= digits[no_increase - 1]:
            no_increase -= 1
        if no_increase == 0:
            return ''

        # 2341 5 7641

        min_big = len(digits) - 1
        while digits[min_big] <= digits[no_increase - 1]:
            min_big -= 1
        # 2341 5 7 6 41    we get index of 5 and index of 5
        digits[no_increase - 1], digits[min_big] = digits[min_big], digits[no_increase - 1]
        # 2341 6 7541
        digits[no_increase:] = digits[len(digits) - 1:no_increase - 1:-1]
        # 2341 6 1457
        return ''.join(digits)

    def nextPalindrome(self, num: str) -> str:
        center = ''
        #1 2 2 1
        n = len(num)
        if n < 4:
            return ''
        # 2
        #1 2 3 2 1
        half_index = n // 2
        if n % 2 != 0:
            center = num[half_index]

        half = num[:half_index]
        next_half = self._nextGreaterElement(half)
        if next_half == '':
            return ''
        return next_half + center + next_half[::-1]