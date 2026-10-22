# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # so we know if they split, that's the LCA.
        # we also know that if we equal one of them, that's the LCA.
        # do we need an insider help function or can we use the function itself? 

        # base case, we don't really ever hit an empty node since we return LCA at a split, or when it equals one of the node vals, since it's guaranteed to be in the tree, right? 
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # NEXT option would be that if either THEY SPLIT or IT IS EQUAL TO EITHER, then we return current node in either case, so ELSE should cover it.
        else:
            return root 