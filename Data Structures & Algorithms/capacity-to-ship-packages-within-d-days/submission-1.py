class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # each day, load ship w/ packages on conveyer build in order given by weights
        # cannot load weight more than MAX weight capacity of ship
        # return the LEAST weight capacity of ship that will result in all packs shipped within x days
        # it's packaged by order, so you can't sort... 
        # sort of like koko bananas problem, we need to utilize the days lim to subtract from
        # we know fro mthe CONSTRAINT it's not gonna be bigger than 500, day can be as low as one. length can be as high 50k
        # so, max would be something like 500 x 50000, with a lowest day of 1, so that's our RIGHT 
        res = (500 * 50000)
        l, r = 1, (500 * 50000)
        while l <= r:
            curCap = (r + l) // 2
            if max(weights) > curCap:
                l = curCap + 1
                continue
            # have to get a rate of burndown
            # inner loop to iterate over weights
            curDays = 1
            curLoad = 0
            for w in weights:
                curLoad += w 
                if curLoad > curCap:
                    curDays += 1
                    curLoad = w
            if curDays <= days:
                res = min(res, curCap)
                r = curCap - 1
            else:
                l = curCap + 1
        return res
                



            
