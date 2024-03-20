from typing import List


class SolutionBruteForce:
    def trap(self, height: List[int]) -> int:
        rain = 0
        size = len(height)
        for i in range(0,size):
            left_max = right_max = 0
            for l in reversed(range(0, i+1)):
                left_max = max(height[l], left_max)
            for r in range(i, size):
                right_max = max(height[r], right_max)
            rain += min(left_max, right_max) - height[i]
        return rain


if __name__ == '__main__':
    solution = SolutionBruteForce()
    trapRain = solution.trap([4,2,0,3,2,5])
    print(trapRain)