# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # if there's no subroot, it's true
        if not subRoot:
            return True

        # if no root with subroot, false
        if not root:
            return False

        # we want to use a helper function and return True when it's evaluated to true
        def isSameTree(a, b):
            if not a and not b:
                return True 
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            # if they both exist and equal vals, we continue them lockstep
            return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)
        
        # now we want to invoke the isSameTree and if it returns true, we want to return True for that subroot
        if isSameTree(root, subRoot):
            return True 
        
        # now we want to invoke isSubTree by searching down left and right nodes if isSameTree isn't currently true, this traverses
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
