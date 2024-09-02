class SolutionDPBruteForce:
    def longestIdealString(self, s: str, k: int) -> int:
        dp_len_at_index = [1] * len(s)
        for right in range(len(s)):
            for left in range(right):
                abs_diff = abs(ord(s[right]) - ord(s[left]))
                if abs_diff <= k:
                    left_seq_with_right = dp_len_at_index[left] + 1
                    dp_len_at_index[right] = max(dp_len_at_index[right], left_seq_with_right)
        return max(dp_len_at_index)


class SolutionDPByEndingCharacter:
    def longestIdealString(self, s: str, k: int) -> int:
        # simply calculate all characters (128)
        dp_seq_length_end_char = [0] * 128
        for ch in s:
            ch_val = ord(ch)
            lower_bound = ch_val - k
            upper_bound_exclude = ch_val + k + 1
            valid_dp_range = dp_seq_length_end_char[lower_bound: upper_bound_exclude]
            dp_seq_length_end_char[ch_val] = max(valid_dp_range) + 1
        return max(dp_seq_length_end_char)


class SolutionDPByEndingCharacterAlphabet:
    def longestIdealString(self, s: str, k: int) -> int:
        dp_seq_length_end_char = [0] * 26
        for ch in s:
            ch_val = ord(ch) - ord('a')
            lower_bound = max(0, ch_val - k)
            upper_bound_exclude = min(ch_val + k, 25) + 1
            valid_dp_range = dp_seq_length_end_char[lower_bound: upper_bound_exclude]
            dp_seq_length_end_char[ch_val] = max(valid_dp_range) + 1
        return max(dp_seq_length_end_char)
