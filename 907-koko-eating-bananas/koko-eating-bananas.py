import math 
class Solution:
    def totalHours(self,piles,speed):
        totalhrs = 0
        for ban in piles:
            totalhrs += math.ceil(ban/speed)
        return totalhrs

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = float('inf')
        while low <= high:
            mid = (low + high ) // 2
            totalhrs = self.totalHours(piles, mid)
            if totalhrs <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans