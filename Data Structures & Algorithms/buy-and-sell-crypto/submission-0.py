class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use two pointers, keep the l on the lowest number found
        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r = r + 1
                continue
            currProfit = prices[r] - prices[l]
            if currProfit > profit:
                profit = currProfit
            r += 1
        return profit
            