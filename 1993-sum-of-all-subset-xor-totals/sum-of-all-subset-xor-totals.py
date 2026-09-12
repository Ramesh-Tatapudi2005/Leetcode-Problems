class Solution:
    def findXorSum(self, ind , xorarray , nums, n,ans):
        if ind >= n:
            xsum = 0
            if xorarray:
                for num in xorarray:
                    xsum = xsum ^ num
            return xsum
            
        not_take =  self.findXorSum(ind + 1, xorarray, nums, n,ans)
        xorarray.append(nums[ind])
        take = self.findXorSum(ind+1 , xorarray, nums,n,ans)
        xorarray.pop()
        return not_take + take
    def subsetXORSum(self, nums: List[int]) -> int:
        xor = []
        ans = 0
        return self.findXorSum(0, xor , nums, len(nums),ans)