class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # expected output is int
        # there is never an empty list
        # there is never a 0 for each pile
        # length of the piile can be up to 10^5 ON2 acceptable
        res = max(piles)
        l, r = 1, max(piles)
        while l <= r:
            m = (l + r) // 2
            # iterate every every pile and accumulate total hours
            curH = 0
            for p in piles:
                curH += math.ceil(p / m)
            if curH > h:
                l = m + 1
            else:
                res = min(m, res)
                r = m - 1
        return res
