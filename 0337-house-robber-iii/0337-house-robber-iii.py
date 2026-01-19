from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {None : 0}
        def dfs(root: TreeNode) -> int:
            if root in memo:
                return memo[root]
            with_parent = root.val
            without_parent = 0
            if root.left:
                with_parent += (dfs(root.left.left) + dfs(root.left.right))
                without_parent += dfs(root.left)
            if root.right:
                with_parent += (dfs(root.right.left) + dfs(root.right.right))
                without_parent += dfs(root.right)

            memo[root] = max(with_parent, without_parent)
            return memo[root]

        return dfs(root)