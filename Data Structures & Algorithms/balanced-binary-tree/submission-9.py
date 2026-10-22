# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # we can do a helper function here to grab height of each side and then compare 
        if not root:
            return True
        isBalanced = True
        def height(node):
            nonlocal isBalanced
            if not node:
                return 0
            # if we find that there is an imbalance AT the node, we return state of false.
            leftH = height(node.left)
            rightH = height(node.right)
            if abs(leftH - rightH) > 1:
                isBalanced = False
            return max(leftH, rightH) + 1
            
        height(root)

        return isBalanced