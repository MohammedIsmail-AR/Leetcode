class Solution(object):
    def containsDuplicate(self, nums):
        n = len(nums)

        # for i in range(n-1):
        #     for j in range (i+1,n):
        #         if nums[i] == nums [j]:
        #                 return True 

        # return False 
        unique = set(nums)
        return len(unique) != len(nums)


     
        