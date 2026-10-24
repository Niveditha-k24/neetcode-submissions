class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=prices[0]
        maximum=0
        for i in range(len(prices)):
            best=prices[i]-low
            maximum=max(maximum,best)
            low=min(low,prices[i])
        return maximum
        