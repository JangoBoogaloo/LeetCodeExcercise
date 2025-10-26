class Solution:
    def majorityElement(self, nums):
        majorityScore = 0
        major = None
        for num in nums:
            if majorityScore == 0:
                major = num
            if num == major:
                majorityScore += 1
            else:
                majorityScore += -1
        return major







