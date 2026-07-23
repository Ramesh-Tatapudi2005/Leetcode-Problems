class Solution:
    def daysneeded(self, arr, cap):
        totaldays = 1
        load = 0
        for w in arr:
            if w + load > cap:
                totaldays += 1
                load = w
            else:
                load += w
        return totaldays
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = -1
        while low < high:
            mid = (low + high) // 2
            noofdays = self.daysneeded(weights, mid)
            if noofdays <= days:
                high = mid 
            else:
                low = mid + 1
        return low