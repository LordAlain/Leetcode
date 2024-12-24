class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        curr = 0
        res = 0

        while l < r:
            curr = (r - l) * min(height[l], height[r])
            res = max (res, curr)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res