# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
                # we can use a prefix to iterate 1 by 1 over preorder to, use the INDICES of inorder from left to middle (current node), and then from mid to end of len(inorder)

        # build out the hashmap so we can keep track of the indices for each node
        inorderMap = {v: i for i, v in enumerate(inorder)}

        # establish prefix to iterate over preorder 
        prefix = 0 

            # helper function with left and right borders
        def build(left, right): 
            nonlocal prefix
            # base case 
            if left > right:
                return
            nodeVal = preorder[prefix]
            mid = inorderMap[nodeVal]
            node = TreeNode(nodeVal) 
            prefix += 1 
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node 

        return build(0, len(inorder) - 1)
