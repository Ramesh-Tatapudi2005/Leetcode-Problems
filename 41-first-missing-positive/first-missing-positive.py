class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [0]*n
        for i in range(n):
            if 0< nums[i] <= n:
                ans[nums[i]-1] = nums[i]
        for i in range(n):
            if ans[i] == 0:
                return i+1
        return n+1