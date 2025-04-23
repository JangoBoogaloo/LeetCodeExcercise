from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combinations: List[str] = []
        current: List[str] = []
        digit_list = list(digits)
        digit_char_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def backtrack(digit_index: int) -> None:
            if digit_index == len(digit_list):
                combinations.append("".join(current))
                return
            digit = digit_list[digit_index]
            char_list = digit_char_map[digit]
            for ch in char_list:
                current.append(ch)
                backtrack(digit_index+1)
                current.pop()

        backtrack(0)
        return combinations


if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations(""))
