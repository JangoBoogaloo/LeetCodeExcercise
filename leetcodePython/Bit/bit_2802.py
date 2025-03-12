class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        # 777747447 = 111101001
        # 1000   = 0b1111101001
        k = k+1
        k_th_binary = bin(k)[3:]
        answer = k_th_binary.replace("0", "4").replace("1", "7")
        return answer
