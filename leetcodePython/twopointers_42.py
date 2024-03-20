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

class SolutionDP:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        if size == 0:
            return 0
        end_index = size - 1
        left_max = [0] * size
        left_max[0] = height[0]
        # max height from left most to index i
        for i in range(1, size):
            left_max[i] = max(height[i], left_max[i-1])

        # max height from right most to index i
        right_max = [0] * size
        right_max[end_index] = height[end_index]
        for i in reversed(range(0, end_index)):
            right_max[i] = max(height[i], right_max[i + 1])
        rain = 0
        for i in range(1, size):
            rain += min(left_max[i], right_max[i]) - height[i]

        return rain


class SolutionTwoPointers:
    def trap(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height)-1
        left_max = right_max = 0
        rain = 0
        while left_pointer < right_pointer:
            # the lowest `wall` is on the left
            if height[left_pointer] < height[right_pointer]:
                # height is lower than left `wall`, so we trap some water
                if height[left_pointer] < left_max:
                    rain += (left_max - height[left_pointer])
                else:
                    # we are getting a new left max wall to trap water
                    left_max = height[left_pointer]
                left_pointer += 1
            else: # the lowest wall is on the right
                if height[right_pointer] < right_max:
                    rain += (right_max - height[right_pointer])
                else:
                    # we are getting a new left max wall to trap water
                    right_max = height[right_pointer]
                right_pointer -= 1

        return rain


if __name__ == '__main__':
    solution = SolutionTwoPointers()
    trapRain = solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print(trapRain)