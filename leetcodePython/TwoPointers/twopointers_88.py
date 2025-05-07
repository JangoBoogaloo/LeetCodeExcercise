class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i1, i2 = m-1, n-1
        i = m + n - 1
        while i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[i] = nums1[i1]
                i1 -= 1
            else:
                nums1[i] = nums2[i2]
                i2 -= 1
            i -= 1
        for j in range(i2, -1, -1):
            nums1[i] = nums2[j]
            i -= 1
