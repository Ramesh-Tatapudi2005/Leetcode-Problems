class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxpro = minpro = ans = nums[0]
        for num in nums[1:]:
            print(maxpro)
            if num < 0:
                maxpro, minpro = minpro , maxpro
            maxpro = max(num, maxpro*num)
            minpro = min(num, minpro*num)
            ans = max(ans, maxpro)
            print(maxpro,ans)
        return ans