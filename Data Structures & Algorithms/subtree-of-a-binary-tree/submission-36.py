# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #trust hellper function and if it doesn't come back True, move down main tree

        if not subRoot:
            return True

        #if no root, but subroot, musit be false
        if not root:
            return False 

        # helper function
        def isSameTree(node, subRoot):
            # base cases 
            if not node and not subRoot:
                return True
            
            if not node or not subRoot:
                return False 

            if node.val != subRoot.val:
                return False

            #otherwise it's likely STILL same val so we continue to check both ends
            
            return (isSameTree(node.left, subRoot.left) and isSameTree(node.right, subRoot.right))

        # now we can check if it's the same.. if it returns FALSE when at same value.. it will STILL retry down left and right IN CASE it does return True at some point. 
        if isSameTree(root, subRoot):
            return True 

        # if it isn't the same we continue down, using OR since we want to check both  sides
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
