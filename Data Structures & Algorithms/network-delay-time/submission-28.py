import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
                # input: times, list of lists, contains (sourceNode, targetNode, weight), n is # of nodes, k is node val that is the network source 

        # so we want to utilize a minHeap here that will help us identify the min time it takes to traverse 
        # we also want to utilize a 'visited' set that lets us know a node has already been activated 
        # we also want to use a hMap that tells use what node: target nodes + weights 
        # want to make sure to put the value we want heap to sort by FIRST 

        # using N as # of nodes, and E as # of edges. we visit every N to build out our hashmap of nodes and neighbors. for every edge of that node, we push it onto the minHeap, and updating a minHeap costs OLog(N), so Time complexity: O(N) + O(ElogN)
        # space complexity = O(N + E) 

        # now let's do the code 
        minHeap = [(0, k)] #initializes source node as first minHeap obj

        # init visited
        visited = set()

        # init time 
        t = 0

        neighbors = defaultdict(list) # since we append each neighbor + weight 

        # populate neighbors 
        for source, target, w in times:
            neighbors[source].append((w, target))

        # while loop through minheap to start with source, and always go route of shortest time
        while minHeap:
            w1, node1 = heapq.heappop(minHeap)
            if node1 in visited: # if node1 already been visited, it's active and this is longer route
                continue 
            visited.add(node1) # if not, add it to visited 
            # update the time 
            t = max(t, w1)
            # now we iterate through its pointers 
            for w2, node2 in neighbors[node1]:
                # if the neighbor node is already in visited, don't add to heap
                if node2 in visited:
                    continue
                # else, add it to heap for visiting
                heapq.heappush(minHeap, (w2 + w1, node2)) # we add both w1 and w2 

        # now we ONLY return the time if it's possible all networks were visited, meaning visited len = n
        return t if len(visited) == n else -1
