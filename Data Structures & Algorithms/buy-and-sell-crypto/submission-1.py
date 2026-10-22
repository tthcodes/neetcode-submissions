class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init two pointers 
        # init initial diff
        # if right pointer is ever lower than the left, move the left to that pointer, move it to right
        l, r = 0, 1
        maxProfit = 0
        while l < r and r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
                continue
            profit = prices[r] - prices[l]
            if profit > maxProfit:
                maxProfit = profit
            r += 1
        return maxProfit
