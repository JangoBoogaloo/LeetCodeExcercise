class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordIndex = 0
        abbrIndex = 0

        while wordIndex < len(word) and abbrIndex < len(abbr):
            if word[wordIndex] != abbr[abbrIndex]:
                if not abbr[abbrIndex].isdigit() or abbr[abbrIndex] == '0':
                    return False
                abbrvCount = 0
                while abbrIndex < len(abbr) and abbr[abbrIndex].isdigit():
                    abbrvCount = abbrvCount * 10 + int(abbr[abbrIndex])
                    abbrIndex += 1
                # we directly jump pointer for word
                wordIndex += abbrvCount
            else:  # we only move pointer when they match
                wordIndex += 1
                abbrIndex += 1

        return wordIndex == len(word) and abbrIndex == len(abbr)

if __name__ == '__main__':
    solution = Solution()
    result = solution.validWordAbbreviation("internationalization", "i5a11o1")
    print(result)