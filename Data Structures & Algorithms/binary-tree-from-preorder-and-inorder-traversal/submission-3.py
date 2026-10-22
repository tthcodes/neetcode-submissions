# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case for returning None when we reach no node
        if not preorder or not inorder:
            return None
        # first element in preorder is awlays ROOT.
        # everyt subsequent sublist of preorder is the next root
        self.inorderMap = {v: i for i, v in enumerate(inorder)}
        
        currRoot = preorder[0]

        mid = self.inorderMap[currRoot]

        # now using the mid, we can re-shape inorder and preorder to pass down 
        # we want to create the newNode 
        root = TreeNode(currRoot)

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:]) # + 1 because index EXCLUSIVE at end.
        return root