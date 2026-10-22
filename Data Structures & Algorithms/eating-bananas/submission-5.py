class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # return the min int (k) such that you can eat all banans within (h) hours
        # init res 
        res = max(piles)
        l, r = 1, res
        while l <= r:
            t = 0
            m = (l + r) // 2
            for p in piles:
                t += math.ceil(p / m)
            if t <= h:
                res = min(m, res)
                r = m - 1
            else:
                l = m + 1
        return res



