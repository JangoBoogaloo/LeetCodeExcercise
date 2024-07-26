class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # 234157641
        digits = list(str(n))
        no_increase = len(digits) - 1

        # 2341 5 7641
        while no_increase - 1 >= 0 and digits[no_increase] <= digits[no_increase - 1]:
            no_increase -= 1
        if no_increase == 0:
            return -1

        # 2341 5 7641

        min_big = len(digits) - 1
        while digits[min_big] <= digits[no_increase - 1]:
            min_big -= 1
        # 2341 5 7 6 41    we get index of 5 and index of 5
        digits[no_increase - 1], digits[min_big] = digits[min_big], digits[no_increase - 1]
        # 2341 6 7541
        digits[no_increase:] = digits[len(digits) - 1:no_increase - 1:-1]
        # 2341 6 1457
        ans = int(''.join(digits))
        return ans if ans < 1 << 31 else -1