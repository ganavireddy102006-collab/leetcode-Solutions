class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            else:
                i=0
                while i<len(nums) and nums[i]<target:
                    i+=1
                nums.insert(i, target)
                return i