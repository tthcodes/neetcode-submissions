"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # init a hashmap that uses original nodes as keys and copies as values
        oldToNew = {}
        # helper function to clone each node and its neighbors
        def clone(node):
            # if the clone already exists in the oldToNew, we return the copy as to not duplicate work
            if node in oldToNew:
                return oldToNew[node] # this returns new copy of it
            
            # if a copy doesn't exist, create it 
            copy = Node(node.val)

            # place copy in hashmap
            oldToNew[node] = copy
            
            # then we want to iterate over node's neighbors and append copies to new node
            for n in node.neighbors:
                copy.neighbors.append(clone(n))
            
            # then we want to return the copy IF it isn't null
            return copy 
        return clone(node) if node else None