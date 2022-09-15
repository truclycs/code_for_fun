class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a = []
        n = len(nums1) + len(nums2)
        mid = n // 2
        i1 = 0
        i2 = 0
        while i1 < len(nums1) or i2 < len(nums2):
            if i1 < len(nums1) and i2 < len(nums2):
                if nums1[i1] < nums2[i2]:
                    a.append(nums1[i1])
                    i1 += 1
                else:
                    a.append(nums2[i2])
                    i2 += 1
            elif i1 < len(nums1):
                a.append(nums1[i1])
                i1 += 1
            else:
                a.append(nums2[i2])
                i2 += 1
            if len(a) == mid + 1:
                break

        if n % 2 != 0:
            return a[mid]

        return ((float)(a[mid]) + (float)(a[mid - 1])) / 2