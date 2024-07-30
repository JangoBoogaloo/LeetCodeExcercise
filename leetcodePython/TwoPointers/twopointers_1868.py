from typing import List


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i1 = i2 = 0
        prodNums = []
        while i1 < len(encoded1) or i2 < len(encoded2):
            base1, freq1 = encoded1[i1]
            base2, freq2 = encoded2[i2]
            if freq1 < freq2:
                new_encode = [base1*base2, freq1]
                if len(prodNums) > 0 and prodNums[-1][0] == new_encode[0]:
                    prodNums[-1][1] += new_encode[1]
                else:
                    prodNums.append(new_encode)
                encoded2[i2] = [base2, freq2-freq1]
                i1 += 1
            elif freq1 > freq2:
                new_encode = [base1*base2, freq2]
                if len(prodNums) > 0 and prodNums[-1][0] == new_encode[0]:
                    prodNums[-1][1] += new_encode[1]
                else:
                    prodNums.append(new_encode)
                encoded1[i1] = [base1, freq1-freq2]
                i2 += 1
            else:
                new_encode = [base1*base2, freq1]
                if len(prodNums) > 0 and prodNums[-1][0] == new_encode[0]:
                    prodNums[-1][1] += new_encode[1]
                else:
                    prodNums.append(new_encode)
                i1 += 1
                i2 += 1
        return prodNums


if __name__ == '__main__':
    sol = Solution()
    sol.findRLEArray([[2,2]], [[1,1],[4,1]])