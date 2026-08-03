class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        while val in nums:
            nums.remove(val)
        k = len(nums)
        # return k