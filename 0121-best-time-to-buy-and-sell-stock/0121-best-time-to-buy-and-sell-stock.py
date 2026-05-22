class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy=prices[0]
        for i in range(len(prices)):
            buy= min(buy,prices[i])
            sell=prices[i]
            profit=max(profit,sell-buy)
        return profit