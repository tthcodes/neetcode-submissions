import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # given list of int
# return an int
# we want to build the negated list so heap gives us the MAX instead of min

        h = [-s for s in stones]

        # now build the heap

        heapq.heapify(h)

        # now max is on top. 
        while len(h) > 1:
            # we know there's at least 2 so pop off 2 heaviest
            x = abs(heapq.heappop(h))
            y = abs(heapq.heappop(h))
            print(x, y)
            
            if x == y:
                continue
            else:
                diff = abs(x - y)
                print('diff', diff)
                heapq.heappush(h, -diff)
            print(h)

        return abs(h[0]) if h else 0
