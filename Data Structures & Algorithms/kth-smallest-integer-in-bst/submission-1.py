# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative approach, so that time/space is O(h + k) 
        stack = [] # this is where we'll stack vals as we go down
        curr = root # establishing a 'tail' 
        while curr or root: # while either of these still exist
            # go down left until it's nont 
            while curr:
                stack.append(curr)
                curr = curr.left 
            # once curr now is at none, last el on stack is cur lowest 
            curr = stack.pop() # pop off stack and make it curr 
            k -= 1
            if k == 0:
                # if k equals 0, we are at the kth
                return curr.val
            # if not, we want to make curr the right side and explore that 
            curr = curr.right 