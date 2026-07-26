class Solution(object):
    def maxFrequency(self, nums, k):
        i = 0
        nums.sort()
        for j in xrange(len(nums)):
            k += nums[j]
            if k < nums[j] * (j - i + 1):
                k -= nums[i]
                i += 1
        return j - i + 1
                 

    
        