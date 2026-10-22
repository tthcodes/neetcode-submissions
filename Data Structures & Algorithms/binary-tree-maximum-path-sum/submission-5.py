# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # return MAX path sum of any non-empty path. Path sum is sum of node values in path. 


        # this kind of reads to me like a problem you can apply 'greedy' on, and just make sure that the current sum through the sequence is non-zero. if it's greater than zero and connect, we can probably add it to the max and continue to compare to best

        # self.best shouild be initialized as the root. 

        best = root.val

        # then we can traverse left and right, and consistently compare the currSum to the best. 
        # we want to not include negative running sums, but how do we incorporate that? from the top or the bottm?

        def pathSum(node):
            if not node:
                return 0 
            
            L = pathSum(node.left)
            R = pathSum(node.right)
            # think i'm missing the aspect of MAXING left vs. right but i need both at the root..
            curSum = (L + R + node.val)

            nonlocal best 

            best = max(curSum, best) 
            # what you're missing here is to RETURN the best max from left and right
            bestSide = max(L, R) + node.val

            return bestSide if bestSide > 0 else 0

        # then need to invoke and return best 

        pathSum(root)

        return best
