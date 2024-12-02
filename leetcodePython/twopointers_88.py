class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        size = range(m+n)[::-1]
        i1 = m-1
        i2 = n-1

        for i in size:
            if i1 < 0:
                nums1[i] = nums2[i2]
                i2 -= 1
                continue
            if i2 < 0:
                nums1[i] = nums1[i1]
                i1 -= 1
                continue
            if nums1[i1] > nums2[i2]:
                nums1[i] = nums1[i1]
                i1 -= 1
            else:
                nums1[i] = nums2[i2]
                i2 -= 1



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    a = [1,2,3,4,None,None,None]
    solution.merge(a, 4, [5,6,7], 3)
    print(a)