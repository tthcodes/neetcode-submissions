# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # set curr to root so we can move along it
        # init a stack
        stack = []
        curr = root 
        # iterate as long as there's a stack or node 
        while curr or stack:
            # now iterate down curr to the left so we append nodes to stack
            while curr:
                stack.append(curr)
                curr = curr.left 
                # now we're appending nodes all the way to the left 
            # now the smallest value should be at the end 
            curr = stack.pop()
            k -= 1 
            # check if k is 0 
            if k == 0:
                return curr.val
            # now that we checked the last left node, we can now check the bottom node's right
            curr = curr.right 