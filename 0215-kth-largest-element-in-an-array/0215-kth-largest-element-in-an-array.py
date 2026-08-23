class Solution(object):
    def findKthLargest(self, nums, k):
        min_val, max_val = min(nums), max(nums)
        
        # Create buckets for every possible number in the range
        count = [0] * (max_val - min_val + 1)
        
        # Count occurrences of each number
        for num in nums:
            count[num - min_val] += 1
            
        # Traverse backward from the highest bucket to find the k-th largest
        for i in range(len(count) - 1, -1, -1):
            k -= count[i]
            if k <= 0:
                return i + min_val