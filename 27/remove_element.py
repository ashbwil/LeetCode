class Solution(object):
    def removeElement(self, nums, val):
        prev = val
        i = 0
        while i < len(nums):
            if nums[i] == prev:
                nums.pop(i)
            else:
                i = i + 1
        return len(nums)