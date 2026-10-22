"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # return the first node 
        # we can make an oldToNew hashmap, this way we can stop infinite recursion and duplicate nodes, as well as reference it to add the newNode to the neighbors attribute 

        oldToNew = {} 

        # we can now make a helper function to actually clone, and that helper function should return the input node 

        def clone(node):
            # edge case for when node is None
            if not node:
                return None
            # we want to simply return the node if it already exists as a copy
            if node in oldToNew:
                return oldToNew[node]

            # create new node, and add to hashmap if it doesn't already exist 
            newNode = Node(node.val) 
            oldToNew[node] = newNode

            # now we iterate through node's neighbors and for each, we want to insert them into newNode's neighbors.

            for n in node.neighbors:
                newNode.neighbors.append(clone(n))

            return newNode

        # now we need to invoke clone and return the newclone's root
        return clone(node)
