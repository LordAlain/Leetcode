class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize the variables
        max_current = max_global = nums[0]

        # Iterate through the array
        for num in nums[1:]:
            max_current = max(num, max_current + num)
            if max_current > max_global:
                max_global = max_current

        return max_global