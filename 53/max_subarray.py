class Solution(object):
    def maxSubArray(self, nums):
        length_max = len(nums)
        maximum = max(nums)
        end = length_max
        final = 0
        start = 0
        
        for x in range(start, end):
            final = final + nums[x]
            if final < 0:
                final = 0
            elif(maximum < final):
                maximum = final
        return maximum
            