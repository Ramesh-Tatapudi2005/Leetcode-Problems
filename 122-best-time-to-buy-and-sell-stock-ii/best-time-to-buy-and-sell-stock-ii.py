class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        stock = 0
        i , j = 0, 1
        while i < n and j < n:
            if prices[i] >= prices[j]:
                stock = prices[j]
                i+=1 
                j += 1
            elif prices[i] < prices[j]:
                ans += prices[j] - prices[i]
                i = j 
                j += 1
        return ans