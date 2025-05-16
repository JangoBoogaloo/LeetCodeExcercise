class Solution316:
    def removeDuplicateLetters(self, s: str) -> str:
        char_stack = []
        seen = set()
        last_occurrence = { c: i for i, c in enumerate(s) }

        for i, ch in enumerate(s):
            if ch not in seen:
                # this is a smaller ch, and it is smaller than stacked item, and stacked item can occur later
                while char_stack and ch < char_stack[-1] and i < last_occurrence[char_stack[-1]]:
                    # let's remove stacked item from set, it will come back later
                    seen.discard(char_stack.pop())
                seen.add(ch)
                char_stack.append(ch)
        return ''.join(char_stack)


class Solution1081:
    def smallestSubsequence(self, s: str) -> str:
        char_stack = []
        seen = set()
        last_occurrence = { c: i for i, c in enumerate(s) }

        for i, ch in enumerate(s):
            if ch not in seen:
                # this is a smaller ch, and it is smaller than stacked item, and stacked item can occur later
                while char_stack and ch < char_stack[-1] and i < last_occurrence[char_stack[-1]]:
                    # let's remove stacked item from set, it will come back later
                    seen.discard(char_stack.pop())
                seen.add(ch)
                char_stack.append(ch)
        return ''.join(char_stack)
