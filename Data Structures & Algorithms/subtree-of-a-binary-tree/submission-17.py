# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # now for the helper function 
        def isSameTree(node, subRoot):
            if not node and not subRoot:
                return True # if they're both at a null, it's the same.
            if not node or not subRoot:
                return False # if one of these is false and the other there, not the same
            if node.val != subRoot.val:
                return False # if vals are diff, they're not the same
            # otherwise we check the rest in lockstep
            return (isSameTree(node.left, subRoot.left) and isSameTree(node.right, subRoot.right))
        # trick is to use both the outer function as recursive and helper function to find SAMENESS
        # if no subroot, it's true
        if not subRoot:
            return True
        if not root:
            return False
        
        if isSameTree(root, subRoot):
            return True 
        
        # if it currently isn't the same tree, CALL the outer function to traverse down
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)) # this checks both sides
