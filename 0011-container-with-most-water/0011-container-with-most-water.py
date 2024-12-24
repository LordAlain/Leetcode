class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_height = max(height)
        curr = 0
        res = 0
    
        # while l < r:
        while max_height * (r - l) > res:
            curr = (r - l) * min(height[l], height[r])
            res = max (res, curr)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res