# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root, subRoot):

        # if not subroot, it's true
        if not subRoot:
            return True

        if not root:
            return False

        # we can use this outer function to traverse amongst the root, make a helper function to lock it in step with subRoot. 

        # here we define isSameTree BEFORE invoking it
        def isSameTree(node, subRoot):

            # if it's both none, return true
            if not node and not subRoot:
                return True

            # if either still exists without the other, it's false
            if not node or not subRoot:
                return False

            # if vals are different, return false
            if node.val != subRoot.val:
                return False

            # else they're the same and we continue, and return the result of BOTH sides
            return isSameTree(node.left, subRoot.left) and isSameTree(node.right, subRoot.right)

        # trust that isSameTree grabs the current node and traverses down 
        if isSameTree(root, subRoot):
            return True

        # if the current root ISN'T same val as subRoot, we traverse down root till we find a val.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
