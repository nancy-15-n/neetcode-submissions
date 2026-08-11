# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            # If both p and q are smaller, go left
            if p.val < root.val and q.val < root.val:
                root = root.left
            # If both p and q are greater, go right
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                # Found the split point → LCA
                return root
