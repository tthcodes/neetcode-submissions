class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = float('-inf')
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
                continue
            prof = prices[r] - prices[l] 
            print(prof)
            res = max(prof, res)
        return res
