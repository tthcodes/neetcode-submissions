# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # return an int = NUMBER of good nodes.
        # good node = path from ROOT to NODE, no nodes with greater val than X's value. 
        # so we have to keep track of each value of every node from root to X (UPPER LIMIT) from top down the X, 
            
        # make a helper function
        def isGood(high, x):

            if not x:
                return 0 

            # we need to keep track of max as we pass it down, and count is counted only when it's valid (cur node against recent max)
            count = 1 if x.val >= high else 0
            
            newHigh = max(high, x.val) # so we can update max as children get bigger than root
            return count + isGood(newHigh, x.left) + isGood(newHigh, x.right)

            # invoke it

        return isGood(float('-inf'), root)	
