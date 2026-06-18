class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # present_dup = None
        # k, i = 0, 0 
        # while i < len(nums):
        #     if nums[i] == present_dup:
        #         nums.pop(i)
        #     else:
        #         k += 1
        #         present_dup = nums[i]
        #         i += 1
        # return k
        k =1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i] 
                k += 1
        return k