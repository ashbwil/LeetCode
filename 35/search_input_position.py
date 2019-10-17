class Solution(object):
    def searchInsert(self, nums, target):
        n = 0
        if target in nums:
            while n < len(nums):
                if nums[n] == target:
                    return n
                else:
                    n = n + 1
        if target > max(nums):
            return (len(nums))
        else:
            while n < len(nums):
                if nums[n] > target:
                    return (n)
                else:
                    n = n + 1
                
            