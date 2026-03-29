class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = -10**5
        i = 0 
        val = 0
        j = len(height) - 1
        while i < j:
            maxi = max(maxi, (j-i) * min(height[i],height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxi