# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum_path_sum = float("-inf")

        def find_path(node: TreeNode) -> int:
            nonlocal maximum_path_sum

            # Base case:
            if not node:
                return 0
            
            left_val = max(find_path(node.left), 0)
            right_val = max(find_path(node.right), 0)

            # Update maximum_path_sum
            maximum_path_sum = max(maximum_path_sum, node.val + left_val + right_val)

            # Return only the larger path to the current node from one side
            return node.val + max(left_val, right_val)
        
        find_path(root)

        return maximum_path_sum