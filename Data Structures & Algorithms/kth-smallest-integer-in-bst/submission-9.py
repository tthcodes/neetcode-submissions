# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # input is the root and k is ith smallest 
        # we can use preorder to append the node to a stack iteratively
        # decrement k and return val of end of stack when k == 0 
        # init stack
        stack = []

        # set the curr to root
        curr = root 

        # while loop that will move down root or pop off the stack while there are still nodes to travel right
        while stack or curr:
            # inner while loop to populate left nodes all the way down onto stack
            while curr:
                stack.append(curr)
                curr = curr.left

        # now that we have all left nodes, we can decrement k by 1
            k -= 1
            
            # update curr to hold least value
            curr = stack.pop()
                
            # if k is 0, we return the last value on the stack
            if k == 0:
                return curr.val
            
            # if k ISN'T 0, we're going to check if the curr node has right children to explore (include their left 
            curr = curr.right 

        # dry run: root = [5, 3, 6, null, 4], k = 2… while should output 3
