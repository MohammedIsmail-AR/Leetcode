class Solution:
    def twoSum(self, nums, target):
        tg ={}
        for i,n in enumerate(nums) :
            diff = target - n 
            if diff in tg :
                return [tg[diff], i]
            tg[n] = i 
        return 
            
     

