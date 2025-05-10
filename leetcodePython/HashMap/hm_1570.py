class SparseVector:
    def __init__(self, nums):
        self.nonZeroMap = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.nonZeroMap[i] = num

    @staticmethod
    def _nonZeroProduct(nonZero1: dict, nonZero2: dict) -> int:
        result = 0
        for i, num in nonZero1.items():
            if i in nonZero2:
                result += num * nonZero2[i]
        return result

    def dotProduct(self, vec):
        if len(self.nonZeroMap) < len(vec.nonZeroMap):
            return self._nonZeroProduct(self.nonZeroMap, vec.nonZeroMap)
        else:
            return self._nonZeroProduct(vec.nonZeroMap, self.nonZeroMap)