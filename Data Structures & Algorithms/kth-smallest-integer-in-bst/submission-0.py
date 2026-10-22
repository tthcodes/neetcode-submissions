# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def kthSmallest(self, root, k):

    # given root of BST, and k, return kth smallest value (1st indexed) among all vals in tree.
    # first instinct is to flatten the tree and sort it
    # only way i can think of to do that is to iterate through the tree and append it to a self stack, then sort.. but that sounds like brute force. 
    # helper function to flatten.. maybe there's an order we can place append so that the lower number is always appended first? that would mean having left append, then actual node, then that node's right but starting from the bottom.

    stack = []

    def flatten(root):
        if not root:
            return 

        flatten(root.left)
        nonlocal stack
        stack.append(root.val)
        flatten(root.right)

    # then we utilize stack and return the index of k after sorting..?

    # invoke it 
    flatten(root)

    return stack[k-1]
