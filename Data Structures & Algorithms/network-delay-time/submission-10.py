import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # we need to find the MINIMUM time it takes for each 
        # node to become activated, if it's not possible
        # then we return -1 
        # times[i] = [sourceNode, targetNode, weight]
        # n = # of nodes, k = node that sends signal 

        # init hashmap, representing the edges, key is node, val is 
            # list of neighbors (weight, targetNode)
        edges = defaultdict(list)

        # now we populate by iterating over times 
        for source, target, weight in times:
            edges[source].append((weight, target))
        
        # init minheap
        minHeap = [(0, k)] # begin with weight it takes for first node, which is 0 time to get there, then k

        # init visited set 
        visited = set()

        # init returned time it takes (least) to get all network
        t = 0 # init at 0 seconds 

        # now while loop for as long as minHeap exists 
        while minHeap:
            # check if it's in visited, if so, continue
            weight, node = heapq.heappop(minHeap)
            if node in visited: #if visited, we've already gotten there faster
                continue
            
            # if we haven't visited, we want to add it to visited
            visited.add(node)
            # add it to heap
            heapq.heappush(minHeap, (weight, node))

            # update the time it takes to get to CURRENT node
            t = max(t, weight)

            # then we want to go down each of its neighbors to add to heap
            for weight2, node2 in edges[node]:
                if node2 not in visited:
                    # push time it takes to get to original node + neighbor, along with neighbor itself onto the minheap.
                    heapq.heappush(minHeap, (weight + weight2, node2))
        return t if len(visited) == n else -1
