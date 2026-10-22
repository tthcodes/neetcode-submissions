# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # we need to evaluate using the TOP root as a reference for low, high borders 
        # helper function to dig in 
        def isValid(node, low, high): # set boundary here
            if not node:
                return True
            if not low < node.val < high:
                return False
            # now we want to invoke it ourselves to keep going down left and right
            return (isValid(node.left, low, node.val) and isValid(node.right, node.val, high))
        
        # now we call it with the infinity bounds 
        return isValid(root, float('-inf'), float('inf'))