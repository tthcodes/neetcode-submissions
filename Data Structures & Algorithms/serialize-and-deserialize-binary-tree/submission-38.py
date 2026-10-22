# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # init a list that will hold each node in preorder 
        res = []
        # helper function that traverses tree in preorder and appends either val of '#' to represent None 
        def dfs(root):
            # base case 
            if not root:
                res.append('#')
                return 
            # then we want to dfs the left before going to right, and we append the current node before doing so
            res.append(str(root.val))    
            
            dfs(root.left)
            dfs(root.right)
            
        # return the joined res as 
        dfs(root)
        return ','.join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # input: string containing serialized tree
		# output: root of the deserialized tree 
		
        # init a pointer 
        i = 0
        
        # split up the string based on the input delimiter ',' 
        tokens = data.split(',') # should split out each node val or '#'

# create helper function that will rebuild out the tree 

        def dfs():
            nonlocal i  

            # base case, if s[i] == '#', we return and accept that node spot as None
            if tokens[i] == '#':
                i += 1 # increment i 
                return 

            node = TreeNode(int(tokens[i]))
            i += 1 # move along preorder 

            # then we declare left and right nodes as the next dfs 
            node.left = dfs() 
            node.right = dfs()

            # we MUST return the node so that we return the node to its left and right
            return node 

        return dfs() 

