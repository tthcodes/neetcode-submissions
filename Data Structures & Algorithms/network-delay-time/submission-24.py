import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # we need the time it takes 
        t = 0

        # we need a heap, so that we account for the min of the current targets 
        minHeap = [(0, k)] # starting with the k source node 

        # we need a visited set, so that we know all nodes that have been visited 
        visited = set()

        # we need a hashmap so that we can keep track of each node's directed neighbros and weight
        neighbors = defaultdict(list)

        # now we iterate to populate
        for source, target, weight in times:
            neighbors[source].append((target, weight))

        # now we'll iterate through the minheap 
        while minHeap:
            w, n1 = heapq.heappop(minHeap)
            # if that node has already been visited, then we can continue 
            if n1 in visited:
                continue 
            
            # otherwise we add to visited, and iterate through its neighbors
            visited.add(n1) 
            # here we want to update the total time it's taken to get to this shortest path
            t = max(t, w) 
            
            
            for n2, w2 in neighbors[n1]:
                # if the neighbor is in visited, we want to skip them
                if n2 in visited:
                    continue
                # otherwise, add to heap since no previous path 
                heapq.heappush(minHeap, (w + w2, n2)) # push w/ total time it takes to get there
        return t if len(visited) == n else -1
