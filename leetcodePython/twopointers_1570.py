class SparseVectorBruteforce:
    def __init__(self, nums):
        self.array = nums

    def dotProduct(self, vec):
        result = 0
        for num1, num2 in zip(self.array, vec.array):
            result += num1 * num2
        return result


class SparseVectorHashSet:
    def __init__(self, nums):
        self.nonzeros = {}
        for i, val in enumerate(nums):
            if val != 0:
                self.nonzeros[i] = val

    def dotProductHelp(self, nonzero1, nonzero2):
        result = 0
        for i, val in nonzero1.items():
            if i in nonzero2:
                result += val * nonzero2[i]
        return result

    def dotProduct(self, vec):
        if len(self.nonzeros) < len(vec.nonzeros):
            return self.dotProductHelp(self.nonzeros, vec.nonzeros)
        else:
            return self.dotProductHelp(vec.nonzeros, self.nonzeros)



class SparseVectorTwoPointers:
    def __init__(self, nums):
        self.pairs = []
        for i, val in enumerate(nums):
            if val != 0:
                self.pairs.append([i, val])

    def dotProduct(self, vec):
        result = 0
        p1, p2 = 0, 0
        while p1 < len(self.pairs) and p2 < len(vec.pairs):
            if self.pairs[p1][0] == vec.pairs[p2][0]:
                result += self.pairs[p1][1] * vec.pairs[p2][1]
                p1 += 1
                p2 += 1
            elif self.pairs[p1][0] < vec.pairs[p2][0]:
                p1 += 1
            else:
                p2 += 1
        return result