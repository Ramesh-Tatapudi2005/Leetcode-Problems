class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if not prices or len(prices) < 2:
        #     return 0
        # dif = [prices[i] - prices[i-1] for i in range(1,len(prices))]
        # print(dif)
        # maxi = gmaxi = 0
        # for i in dif:
        #     maxi = max(i,i+maxi)
        #     gmaxi = max(maxi,gmaxi)
        # return gmaxi
        minsp = float('inf')
        max_profit = 0
        for cur_price in prices:
            max_profit = max(max_profit, cur_price- minsp)
            if cur_price < minsp:
                minsp = cur_price
        return max_profit