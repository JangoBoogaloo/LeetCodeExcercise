class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordIndex, abbrIndex = 0, 0
        while wordIndex < len(word) and abbrIndex < len(abbr):
            if word[wordIndex] == abbr[abbrIndex]:
                wordIndex += 1
                abbrIndex += 1
                continue
            if not abbr[abbrIndex].isdigit() or abbr[abbrIndex] == "0":
                return False
            jump = 0
            while abbrIndex < len(abbr) and abbr[abbrIndex].isdigit():
                jump = jump*10 + int(abbr[abbrIndex])
                abbrIndex += 1
            wordIndex += jump
        return wordIndex == len(word) and abbrIndex == len(abbr)




