# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # passing down the value of the root is critical to making sure it's valid multiple levels up
        # we can use a node pass, high cap, low cap 
        # we can use a helper function to validate, then return its validity for both sides of node

        def isValid(node, low, high):
            # here we ensure node is between low and high
            if not node:
                return True
            if low < node.val < high:
                return (isValid(node.left, low, node.val) and isValid(node.right, node.val, high))
            else:
                return False

        # now we call isValid
        return (isValid(root.left, float('-inf'), root.val) and isValid(root.right, root.val, float('inf')))
