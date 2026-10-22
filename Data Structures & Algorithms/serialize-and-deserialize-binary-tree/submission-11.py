# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        nodeList = []
        def preorder(node):
            if not node:
                nodeList.append('#')
                return 
            
            nodeList.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ','.join(nodeList)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodeList = data.split(',')
        ind = 0
        def build():
            nonlocal ind
            nodeVal = nodeList[ind]
            ind += 1

            if nodeVal == '#':
                return None
                
            node = TreeNode(int(nodeVal))
            node.left = build()
            node.right = build() 

            return node 
        
        return build()