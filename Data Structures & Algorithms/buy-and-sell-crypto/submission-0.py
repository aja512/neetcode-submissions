class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = prices[0]
        maxPrice = 0

        for i in range(1, len(prices)):
            maxPrice = max(maxPrice, prices[i] - curr)
            curr = min(curr, prices[i])
        
        return maxPrice