# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 1
        def dfs(root: TreeNode, prev: int) -> None:
            nonlocal good_nodes
            if not root:
                return None
            if root.val >= prev:
                good_nodes += 1
            
            dfs(root.left, max(prev, root.val))
            dfs(root.right, max(prev, root.val))
        
        dfs(root.left, root.val)
        dfs(root.right, root.val)
        return good_nodes