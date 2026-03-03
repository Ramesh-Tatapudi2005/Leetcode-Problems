class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        s =  0
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            l , r = i + 1, n - 1
            while l < r:
                s = nums[l] + nums[r] + nums[i]
                if s < 0 : l += 1
                elif s > 0 : r -= 1
                else:
                    res.append([nums[i], nums[l],nums[r]])
                    l+= 1 
                    r -= 1
                    while l < r and nums[l] == nums[l-1] : l += 1
                    while r > l and  nums[r] == nums[r+1] : r-= 1
        return res