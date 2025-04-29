class Solution:
    @staticmethod
    def _cost(ch1: str, ch2:str) -> int:
        diff = abs(ord(ch1) - ord(ch2))
        return min(diff, 26 - diff)

    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        sLength = len(s)
        op_start_end_length = [[[0] * sLength for _ in range(sLength)] for _ in range(k+1)]
        for i in range(sLength):
            for op in range(k+1):
                op_start_end_length[op][i][i] = 1

        for op in range(k + 1):
            for end in range(1, sLength):
                for start in range(end-1, -1, -1):
                    if s[end] == s[start]:
                        op_start_end_length[op][start][end] = op_start_end_length[op][start+1][end-1] + 2
                    else:
                        op_start_end_length[op][start][end] = max(op_start_end_length[op][start+1][end], op_start_end_length[op][start][end-1])
                        opCost = self._cost(s[start], s[end])
                        if opCost <= op:
                            op_start_end_length[op][start][end] = max(op_start_end_length[op][start][end], op_start_end_length[op-opCost][start+1][end-1] + 2)
        return op_start_end_length[k][0][sLength-1]