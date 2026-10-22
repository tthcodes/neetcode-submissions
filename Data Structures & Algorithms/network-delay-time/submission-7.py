import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # BFS solution, Min head needed.
        # in minheadp, keep 2 values: 1 pathLength, 2 actualNode
        # you want to begin with a dict that holds key as source node, and value as (dest node, weight)
        edges = defaultdict(list)

        # populate edges with source node = [[weight, node], ...]
        for u, v, w in times:
            edges[u].append((w, v))

        heap = [(0, k)] # begin with weight to get to node, and node

        visited = set()

        t = 0 # time it takes 

        while heap:
            w, node = heapq.heappop(heap)
            if node not in visited:
                t = max(t, w)
                visited.add(node)

                for w2, node2 in edges[node]:
                    if node2 not in visited:
                        heapq.heappush(heap, (w + w2, node2))
            else:
                continue

        return t if len(visited) == n else -1