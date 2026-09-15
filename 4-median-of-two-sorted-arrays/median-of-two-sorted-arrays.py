class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        d=nums1+nums2
        d.sort()
        n=len(d)
        if n%2==0:
            return (d[n//2-1]+d[n//2])/2.0
        else:
            return d[n//2]