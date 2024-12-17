class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        hs = set(nums)
        maxlen = 0

        for num in hs:
            if (num - 1) not in hs:
                length = 1
                while (num + length) in hs:
                    length += 1
                maxlen = max(maxlen, length)
        return maxlen