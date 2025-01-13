class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tot = sum(range(len(nums)+1))
        n = sum(nums)
        # print(tot)
        # print(n)
        return tot - n