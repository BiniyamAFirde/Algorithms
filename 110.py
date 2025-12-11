# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node):
            """
            Returns height of subtree if balanced, otherwise -1
            """
            # Base case: empty node has height 0 and is balanced
            if not node:
                return 0
            
            # Check left subtree
            left_height = check_balance(node.left)
            if left_height == -1:  # Left subtree is unbalanced
                return -1
            
            # Check right subtree
            right_height = check_balance(node.right)
            if right_height == -1:  # Right subtree is unbalanced
                return -1
            
            # Check if current node is balanced
            if abs(left_height - right_height) > 1:
                return -1  # Current node is unbalanced
            
            # Return height of current subtree
            return 1 + max(left_height, right_height)
        
        # The tree is balanced if check_balance doesn't return -1
        return check_balance(root) != -1
