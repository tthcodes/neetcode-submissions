import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # n = number of nodes given,  1 -> n
        # times, list of travel times as directed edges
            # times[i] = (ui, vi, wi), u = source, v = target, w = weight/time
        # k = node value that we send signal from 
        # initialize needed data structures
        visited = set()
        minHeap = [(0,k)] # begin with 1st node which takes 0 time to get to
        t = 0
        edges = defaultdict(list) # will store neighbors 

        # populate edges
        for source, target, weight in times:
            edges[source].append((target, weight))

        # now we want to go through the heap and visit each node 
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            # see if this has been visited before
            if n1 in visited:
                continue
            # other wise, add to visited and update time
            visited.add(n1)
            t = max(t, w1)
            # now iterate through neighbors and calculate time to get to them
            for n2, w2 in edges[n1]:
                # add it to the heap so that we can also visit it 
                # its weight will be current popped node + neighbor weight, which 
                # represents the time total it took to get to the neighbor once we get there
                heapq.heappush(minHeap, (w2 + w1, n2))
        return t if len(visited) == n else -1 

        # time complexity = E * log(v), where e is edges, and v is num of nodes 
        # space = V being num of nodes, since we store up to that many in edges dict
