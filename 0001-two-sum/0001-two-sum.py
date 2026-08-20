class Solution:
    def twoSum(self, nums, target):
        l,r = 0,0
        for l in range(len(nums)):
            for r in range(l + 1,len(nums)):
                if nums[l]+nums[r] == target :
                    return [l,r]

         