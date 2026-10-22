# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root):
# we need to pass down the ceiling, and return count 
# helper function so that it can pass down 2 args, root and ceiling
        def isGood(ceil, node):
            if not node:
                return 0
            count = 1 if node.val >= ceil else 0
            newCeil = max(ceil, node.val)
            return (count + isGood(newCeil, node.left) + isGood(newCeil, node.right))
        # invoke it 

        return isGood(float('-inf'), root)
            
        # [2, 4, 6] = 3 
            # 2 > -inf -> count is 1
            # 4 > 2 -> count is 1 
            # 6 > 2 -> count is 1 
            # -> returns up to 3 
        # [] = 0 
            # returns 0 
