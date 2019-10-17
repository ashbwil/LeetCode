class Solution(object):
    def removeDuplicates(self, nums):
        prev = None
        i = 0
        while i < len(nums):
            if nums[i] == prev:
                nums.pop(i)
            else:
                prev = nums[i]
                i = i + 1
        return len(nums)
                