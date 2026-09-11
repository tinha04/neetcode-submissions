class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minB = prices[0]

        for p in prices:
            maxProfit = max(maxProfit, p - minB)
            minB = min(minB, p)

        return maxProfit