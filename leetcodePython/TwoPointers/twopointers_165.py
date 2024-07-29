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