class Solution:
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     set_nums = set(nums)
    #     res = []
    #     for i in range(1, len(nums) + 1):
    #         if i not in set_nums:
    #             res.append(i)
    #     return res

    #     # return set(range(1,len(nums)+1)) - set(nums)

    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     for num in nums:
    #         index  = abs(num) - 1
    #         nums[index] = -abs(nums)[index]

    #     result = []
    #     for i in range(0, len(nums)):
    #         if nums[i] > 0:
    #             result.append(i + 1)

    #     return result
    

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        bucket = [0] * (len(nums)+1)

        for i in range(0, len(nums)):
            bucket[nums[i]] = 1
        
        result = []
        for i in range(1, len(bucket)):
            if bucket[i] == 0:
                result.append(i)
        
        return result
        """
        Time complexity is O(n) and space complexity is O(n)
        """