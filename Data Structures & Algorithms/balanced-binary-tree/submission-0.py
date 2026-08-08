# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function returns height if balanced, else -1
        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # If left or right subtree is unbalanced, propagate -1
            if left_height == -1 or right_height == -1:
                return -1
            
            # If difference in height > 1, mark unbalanced
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return height of current node
            return 1 + max(left_height, right_height)
        
        return dfs(root) != -1
