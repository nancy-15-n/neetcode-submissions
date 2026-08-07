# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def depth(node):
            if not node:
                return 0
            # Recursively find left and right subtree heights
            left_height = depth(node.left)
            right_height = depth(node.right)

            # Update max diameter at this node
            self.max_diameter = max(self.max_diameter, left_height + right_height)

            # Return height of subtree
            return 1 + max(left_height, right_height)

        depth(root)
        return self.max_diameter
