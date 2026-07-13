class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxPrice = 0
        now = prices[0]

        for i in range(1, len(prices)):
            mxPrice = max(mxPrice, prices[i] - now)
            now = min(now, prices[i])
        return mxPrice
