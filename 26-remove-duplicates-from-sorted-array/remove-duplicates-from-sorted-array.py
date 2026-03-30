class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = None 
        k,i = 0,0
        while i < len(nums):
            if nums[i] == p:
                nums.pop(i)
            else:
                k += 1
                p = nums[i]
                i += 1
        return k