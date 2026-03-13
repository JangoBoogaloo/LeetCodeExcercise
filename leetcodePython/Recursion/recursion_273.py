class Solution:
    _BELOW_TEN = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    _BELOW_TWENTY = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    _BELOW_HUNDRED = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        return self._toString(num)

    def _toString(self, num:int) -> str:
        if num < 10:
            return self._BELOW_TEN[num]
        if num < 20:
            return self._BELOW_TWENTY[num - 10]
        if num < 100:
            return self._BELOW_HUNDRED[num // 10] + (" " + self._toString(num % 10) if num % 10 != 0 else "")
        if num < 1000:
            return self._toString(num // 100) + " Hundred" + (" " + self._toString(num % 100) if num % 100 != 0 else "")
        if num < 1000000:
            return self._toString(num // 1000) + " Thousand" + (" " + self._toString(num % 1000) if num % 1000 != 0 else "")
        if num < 1000000000:
            return self._toString(num // 1000000) + " Million" + (" " + self._toString(num % 1000000) if num % 1000000 != 0 else "")
        return self._toString(num // 1000000000) + " Billion" + (" " + self._toString(num % 1000000000) if num % 1000000000 != 0 else "")






