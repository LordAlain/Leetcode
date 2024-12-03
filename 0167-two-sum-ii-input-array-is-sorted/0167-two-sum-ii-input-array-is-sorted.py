class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l<r:
            tsum = numbers[l] + numbers[r]
            if tsum > target:
                r -= 1
            elif tsum < target:
                l += 1
            else:
                break
        return [l+1, r+1]