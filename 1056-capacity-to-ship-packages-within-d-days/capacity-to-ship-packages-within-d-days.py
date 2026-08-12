class Solution:
    def calcdays(self, arr, cap):
        days = 1
        load = 0 
        for w in arr:
            if load + w > cap:
                days+= 1
                load = w
            else:
                load += w
        return days
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = (low + high) // 2
            totaldays = self.calcdays(weights,mid)
            if totaldays <= days:
                high = mid 
            else:
                low = mid + 1
        return low