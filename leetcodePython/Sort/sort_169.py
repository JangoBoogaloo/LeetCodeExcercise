class Solution:
    def majorityElement(self, nums):
        count = 0
        major = None
        # major count > len(nums) / 2, so eventually the major count will be > 0 even if we subtract non-major count
        for num in nums:
            if count == 0:
                major = num
            if num == major:
                count += 1
            else:
                count += -1

        return major