class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        max_digit_index = -1
        small_index, large_index = -1, -1
        for i in range(len(num_str) - 1, -1, -1):
            if max_digit_index == -1 or num_str[i] > num_str[max_digit_index]:
                max_digit_index = i
            elif num_str[i] < num_str[max_digit_index]:
                small_index = i
                large_index = max_digit_index

        if small_index != -1 and large_index != -1:
            num_str[small_index], num_str[large_index] = num_str[large_index], num_str[small_index]

        return int("".join(num_str))
