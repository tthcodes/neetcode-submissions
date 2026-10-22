# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def serialize(self, root):
        # return str
        # maybe some kind of delimiter? i think we can visit each node and order it in preorder 
        # create list first, then combine into a str.
        preList = []

        def preorder(node):
            nonlocal preList
            if not node:
                preList.append('#')
                return 
            # append current node before going down to left, then right 
            preList.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        # need to invoke 
        preorder(root)
        # now this should populate preList with a list of preorder with # at each null

        return ','.join(preList) # this should return a strung delimited by commas, and null represents nulls


    def deserialize(self, data):
        # now we can populate this recursively using the pre += 1 trick until data no longer has length/runs out of bounds 
        # wait do we even need this if nulls are already in place? maybe to move along the list?

        dataList = data.split(',')

        prefix = 0

        def recreate():
        # now we use prefix and datalist to populate with the fact that # means empty, and then any other element is a true val, turning it into a node

            nonlocal prefix

            token = dataList[prefix]
            prefix += 1 # increment unconditionally.. but how do we stop? 
            if token == '#':
                return None
            # else we turn it into a node
            currNode = TreeNode(int(token))
            currNode.left = recreate()
            currNode.right = recreate()

            return currNode
    
        return recreate()
