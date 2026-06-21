class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        dif = [prices[i] - prices[i-1] for i in range(1,len(prices))]
        maxi = gmaxi = 0
        for i in dif:
            maxi = max(i,i+maxi)
            gmaxi = max(maxi,gmaxi)
        return gmaxi