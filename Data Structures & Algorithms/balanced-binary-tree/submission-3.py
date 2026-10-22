# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # make a global boolean maybe?
        self.balanced = True # start a true, change if diff too much

        #need helper function to determine heights and if diff of heights ever over 1, return false

        def height(root):
            # base case
            if not root:
                return 0
            leftH, rightH = height(root.left), height(root.right)
            if abs(rightH - leftH) > 1: 
                self.balanced = False
            return max(leftH, rightH) + 1
        height(root)

        # return the boolean
        return self.balanced  
