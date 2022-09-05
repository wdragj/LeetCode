# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # In-Order Traversal
        # Left > Node > Right
        
        inorder = []
        
        def IOT(node):
            # If node is empty return None
            if not node: return None
            
            # Check left
            if node.left: 
                IOT(node.left)
            
            # Check Node
            inorder.append(node.val)
            
            # Check right
            if node.right:
                IOT(node.right)
        
        IOT(root)
        return inorder