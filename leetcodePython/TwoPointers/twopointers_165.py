class SolutionSplit:
    def compareVersion(self, version1: str, version2: str) -> int:
        num1_list = version1.split('.')
        num2_list = version2.split('.')
        n1, n2 = len(num1_list), len(num2_list)
        for i in range(max(n1, n2)):
            num1 = int(num1_list[i]) if i < n1 else 0
            num2 = int(num2_list[i]) if i < n2 else 0
            if num1 != num2:
                return 1 if num1 > num2 else -1
        return 0


class SolutionTwoPointers:
    def _get_next_chunk(self, version: str, length: int, start: int) -> tuple[int, int]:
        if start > length - 1:
            return 0, start
        end = start
        while end < length and version[end] != '.':
            end += 1
        num = -1
        if end != length - 1:
            num = int(version[start:end])
        else:
            num = int(version[start:length])
        start = end + 1
        return num, start

    def compareVersion(self, version1: str, version2: str) -> int:
        len1, len2 = len(version1), len(version2)
        i1, i2 = 0, 0
        while i1 < len1 or i2 < len2:
            num1, i1 = self._get_next_chunk(version1, len1, i1)
            num2, i2 = self._get_next_chunk(version2, len2, i2)
            if num1 != num2:
                return 1 if num1 > num2 else -1
        return 0


if __name__ == '__main__':
    sol = SolutionTwoPointers()
    sol.compareVersion('1.0.1', '1')