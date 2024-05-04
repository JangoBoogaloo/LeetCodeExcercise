from typing import List
from collections import deque

class SolutionDequeStorage:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = deque()
        suffix_prod = deque()
        run_prod = 1
        for num in nums[:-1]:
            run_prod *= num
            prefix_prod.append(run_prod)

        run_prod = 1
        for num in reversed(nums[1:]):
            run_prod *= num
            suffix_prod.appendleft(run_prod)

        ans = [suffix_prod.popleft()]

        for i in range(1, len(nums)-1):
            ans.append(prefix_prod.popleft()*suffix_prod.popleft())
        ans.append(prefix_prod.popleft())

        return ans


class SolutionInplace:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prefix_prod = 1
        for num in nums:
            ans.append(prefix_prod)
            prefix_prod *= num
        suffix_prod = 1
        i = len(nums) - 1
        for num in reversed(nums):
            ans[i] *= suffix_prod
            suffix_prod *= num
            i -= 1
        return ans


if __name__ == "__main__":
    sol = SolutionDequeStorage()
    res = sol.productExceptSelf([-1,1,0,-3,3])
    print(res)
    sol = SolutionInplace()
    res = sol.productExceptSelf([-1,1,0,-3,3])
    print(res)