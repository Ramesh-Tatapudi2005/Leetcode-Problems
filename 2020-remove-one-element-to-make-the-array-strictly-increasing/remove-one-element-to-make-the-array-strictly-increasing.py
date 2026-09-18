class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        ind = -1
        count = 0
        n = len(nums)
        for i in range(n - 1):
            if nums[i] >= nums[i+1]:
                ind = i
                count += 1
            
        if count == 0:
            return True
        if count == 1:
            if ind == 0 or ind == n-2:
                return True
            if nums[ind-1] < nums[ind+1] or (ind+2 < n and nums[ind] < nums[ind+2]):
                return True
        return False
