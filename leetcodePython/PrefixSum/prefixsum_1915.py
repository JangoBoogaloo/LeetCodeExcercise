class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0]*1024
        count[0] = 1
        res = curr = 0
        for ch in word:
            shift_count = ord(ch)-ord('a')
            # 100..... (shift count number of 0)
            ch_bit = 1 << shift_count
            curr = curr ^ ch_bit
            res += count[curr]
            count[curr] += 1
            a, j = 0, 10
            for ch_i in range(a, j):
                ch_bit = 1 << ch_i
                tmp = curr ^ ch_bit
                res += count[tmp]

        return res