class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t = 0
        for i in range(len(nums)):
            t = nums[i] ^ t
        return t