class Solution(object):
    def findPeakElement(self, nums):
        high=nums[0]
        index=0
        for i in range(len(nums)):
            if nums[i]>high:
                high=nums[i]
                index=i
        return index

