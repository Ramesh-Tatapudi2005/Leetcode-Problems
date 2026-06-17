class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        b = 0
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                b += 1
        return b <= 1