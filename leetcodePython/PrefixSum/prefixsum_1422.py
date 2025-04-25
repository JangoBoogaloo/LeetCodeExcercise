class SolutionTwoPass:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeros = 0
        ans = 0
        for ch in s[:-1]:
            if ch == '1':
                ones -= 1
            else:
                zeros += 1
            ans = max(ans, zeros + ones)
        return ans

class SolutionOnePass:
    def maxScore(self, s: str) -> int:
        zeros = 0
        left_ones = 0
        best = float('-inf')
        for ch in s[:-1]:
            if ch == '1':
                left_ones += 1
            else:
                zeros += 1
            best = max(best, zeros - left_ones)

        # total ones actually equal to left_ones after we iterate through
        total_ones = left_ones
        if s[-1] == '1':
            total_ones += 1

        # Max(left_zero - left_ones) + right_ones + left_ones = Max(left_zero + right_ones)
        return best + total_ones