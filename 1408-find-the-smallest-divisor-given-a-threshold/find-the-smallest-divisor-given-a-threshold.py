import math
class Solution:
    def divisorSum(self,nums, divisor):
        Sum = 0
        for num in nums:
            Sum += math.ceil(num/divisor)
        return Sum

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ind = 0
        while low <= high:
            mid = (low + high) // 2
            divisorsum = self.divisorSum(nums,mid)
            if divisorsum <= threshold:
                ind = mid
                high = mid - 1
            else:
                low = mid + 1
        return ind
