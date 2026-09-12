class Solution:
    def findXorSum(self, ind , current_xor , nums, n,ans):
        if ind >= n:
            return current_xor
        not_take =  self.findXorSum(ind + 1, current_xor, nums, n,ans)
        take = self.findXorSum(ind+1 , current_xor ^ nums[ind], nums,n,ans)
        return not_take + take
    def subsetXORSum(self, nums: List[int]) -> int:
        xor = 0
        ans = 0
        return self.findXorSum(0, xor , nums, len(nums),ans)