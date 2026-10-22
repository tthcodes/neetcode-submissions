# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # given root, return max path sum of any non-empty path 
        # we can ignore any negatives 

        # establish max Sum
        curMax = root.val # set it to root.val, not 0 since all neg nums possible

        def maxPath(node):
            if not node:
                return 0 # for none, return 0 value
            
            # we need to add the value to greatest side 
            leftSum = maxPath(node.left)
            rightSum = maxPath(node.right)

            # we need to represent the current best maxpath AT THIS NODE as well. this is what's compared to curMax
            nodeMax = leftSum + rightSum + node.val
            bestSide = max(leftSum, rightSum) # this is what is returned upwards to represent best max path per node.

            # then we compare the sum of both sides + curNode to curmax
            nonlocal curMax
            curMax = max(curMax, nodeMax) 

        # what gets returned is the bestside + node.val
        # only return if it's a netpositive, otherwise we don't want to add it to the path.
            if (bestSide + node.val) > 0:
                return bestSide + node.val 
            else:
                return 0
        maxPath(root)

        # now curMax should hold answer 
        return curMax
