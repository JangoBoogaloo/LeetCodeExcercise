class StockSpanner:
    def __init__(self):
        self._decreasePriceDayStack = [0]
        self._MAX_PRICE = float("inf")
        self._dayPrice = {0: self._MAX_PRICE}
        self._currentDay = 1

    def next(self, price: int) -> int:
        while self._decreasePriceDayStack and price >= self._dayPrice[self._decreasePriceDayStack[-1]]:
            self._dayPrice.pop(self._decreasePriceDayStack.pop())
        days = self._currentDay - self._decreasePriceDayStack[-1]
        self._decreasePriceDayStack.append(self._currentDay)
        self._dayPrice[self._currentDay] = price
        self._currentDay += 1
        return days
