"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # init map
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            # else it's not currently created so make new copy
            copy = Node(node.val)

            # you need to also populate the map with the new copy sincei t's created
            oldToNew[node] = copy

            # then populate its neigbors using recursion
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy
        
        return dfs(node)