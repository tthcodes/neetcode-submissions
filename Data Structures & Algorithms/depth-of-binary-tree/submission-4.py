# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth=0) -> int:
        #how do i make it so that we continuously count as we go down?
# need a base case
        if not root:
            return 0

        # we trust that these return the max depth and then return that result, which should be a num
        leftMaxDepth = self.maxDepth(root.left, depth) 
        rightMaxDepth = self.maxDepth(root.right, depth)

        return max(leftMaxDepth, rightMaxDepth) + 1

        # my idea is that you can use recursion to go down levels and increment the levels, then as you return the levels back up, you compare the max between the path right and left returned, and return the biggest number.
