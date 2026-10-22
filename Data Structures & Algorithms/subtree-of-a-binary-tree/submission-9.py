# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    # don't rewrite, reuse 

    def sameTree(self, p, q):

    # the key is the have returns that signify they're currently the same
    # then keeping them lockstep when evaluating 
    # THEN using the AND for both side returns 

    # one thing i'm wondering, do i compare the length of inserted roots off the rip or is it sufficient my base cases do that for me? 

        if not p and not q: #if they both don't exist at this level, they're the same 
            return True

        if not p and q:
            return False 

        if not q and p:
            return False

        # i feel like this was different than the solution but I need to check both equality and inequality if they both exist.. 
        if p and q:
            if p.val != q.val:
                return False

        return (self.sameTree(p.right, q.right) and self.sameTree(p.left, q.left)) 

    # does going right first break it? 

    # p = [1, 2, null], q = [1, 2, 3].. this comes out to false on the first p.right q.right. 
    # p = [], q = [].. this comes out True on the first iteration 

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
	    # we need to see if subroot exists
        if not subRoot:
            return True # nothing means it's always a subroot
        # if subroot exists but NO root, definitely false
        if not root:
            return False
        
        # now here is where we COMPARE, and if not we move down ROOT, not subroot.
        if self.sameTree(root, subRoot): # this call will return True or False for same tree.
            return True 
        
        # IF THEY'RE NOT THE SAME, call isSubtree again going down left and right
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

