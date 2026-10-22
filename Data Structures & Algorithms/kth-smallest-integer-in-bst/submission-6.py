# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left # we're going all the way down and to the left 
            #not that curr = NONE, we change the curr value to end of stack (last valid)
            curr = stack.pop()
            # now we check k's value
            k -= 1
            if k == 0:
                return curr.val
            # if k != 0, we continue, and check the right branch 
            curr = curr.right 
            