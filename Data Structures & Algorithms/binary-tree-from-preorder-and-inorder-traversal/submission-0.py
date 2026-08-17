# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in inorder for O(1) lookup
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Pointer to track root position in preorder
        self.pre_idx = 0
        
        def helper(left, right):
            # Base case: no elements to construct
            if left > right:
                return None
            
            # Root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            
            # Build left and right subtrees
            root.left = helper(left, inorder_map[root_val] - 1)
            root.right = helper(inorder_map[root_val] + 1, right)
            
            return root
        
        return helper(0, len(inorder) - 1)
