class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = rmax = 0
        left, right = 0, len(height) - 1
        water = 0
        while left < right:
            while left < right and height[left] <= height[right]:
                lmax = max(lmax, height[left])
                water += lmax - height[left]
                left += 1
            while left < right and height[right] < height[left]:
                rmax = max(rmax, height[right])
                water += rmax - height[right]
                right -=1 
        return water 