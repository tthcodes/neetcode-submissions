# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # i feel like this can be a recursion problem? 
        # base case, when val is none, return
        if not root:
            return None
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        # now that we trust it's inverting, we must do it ourselves
        newRight, newLeft = root.left, root.right
        root.left, root.right = newLeft, newRight

        return root
