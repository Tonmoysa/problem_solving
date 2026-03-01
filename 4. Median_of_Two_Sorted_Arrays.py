class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        marge = sorted(nums1 + nums2)
        print(marge)
        n = len(marge)
        if n % 2 == 1:
            return marge[n // 2]
        else:
            return marge[n // 2 - 1] + marge[n // 2] /2


obj = Solution()
result = obj.findMedianSortedArrays(nums1=[10, 20, 40, 30, 4], nums2=[4, 7, 9])
print(result)
