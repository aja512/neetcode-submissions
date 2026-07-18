class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        now, hold, reset = float('-inf'), float('-inf'), 0

        for p in prices:
            prev = now 
            now = hold + p
            hold = max(hold, reset - p)
            reset = max(reset, prev)
        
        return max(now,reset)