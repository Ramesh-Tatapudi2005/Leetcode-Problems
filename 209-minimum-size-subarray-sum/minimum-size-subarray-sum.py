class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        i = 0
        minl = float('inf')
        for j in range(len(nums)):
            s += nums[j]
            while s >= target:
                minl = min(minl,j-i+1)
                s -= nums[i]
                i += 1
        return 0 if minl == float('inf') else minl
