class Solution:
    def sumofdigits(self, num):
        listSum = list(str(num))
        sum = 0
        for num in listSum:
            sum += int(num)
        return sum
            
    def maximumSum(self, nums: List[int]) -> int:
        nums.sort()
        has = {}
        ans = -1
        for num in nums:
            digitsum = self.sumofdigits(num)
            if digitsum in has:
                ans = max(has[digitsum] + num, ans)
            has[digitsum] = num
        return ans