class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        flags = [False] * (len(nums) +1)
        for num in nums :
            flags[num] = True
        for i in range(len(nums) +1):
            if not flags[i]:
                return i
        return -1