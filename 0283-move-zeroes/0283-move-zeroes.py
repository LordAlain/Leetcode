class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) < 2:
            pass
        index = 0

        for n, val in enumerate(nums):
            if val != 0:
                nums[index] = val
                index += 1

        while index < len(nums):
            nums[index] = 0
            index += 1