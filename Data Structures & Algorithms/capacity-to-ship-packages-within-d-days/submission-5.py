class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # input is a list of weights, MUST go in order, and the capacity CANNOT be lower than a single weight.
        # output is an integer, which is the least weight capacity needed to ship within days 

        # init current lowest weight, we can begin this at the sum of all weights.
        leastCapacity = sum(weights)

        # then we can create a helper function that will determine if a given weight capacity can ship within X days, and we'll use binary search to try lower amounts 
        def canShip(cap, days):
            # init a currDay
            currDays = 1 
            
            # init a currLoad
            currLoad = 0
            
            # iterate through weights 
            for w in weights:
                if currLoad + w > cap: # if next weight added goes over, reset currLoad, add, increase day 
                    currDays += 1
                    currLoad = w 
                else:
                    currLoad += w 
            # after loading all weights, return if curreny run of days greater thwn days
            return currDays <= days 

        # the least possible weight is the max of all weights, while sum is highest we can go because it can all be shipped in the first day.
        l, r = max(weights), sum(weights) 

        # start binary search loop
        while l <= r:
            m = (l + r) // 2
            # now see if the current m can ship, if so, lower it. if not, increase m
            if canShip(m, days):
                # compare least capacity to current 
                leastCapacity = min(leastCapacity, m)
                r = m - 1
            else:
                l = m + 1

        # return least
        return leastCapacity
