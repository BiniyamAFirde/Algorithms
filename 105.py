
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # First element of preorder is the root
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Find root position in inorder
        root_idx = inorder.index(root_val)
        
        # Left subtree: elements before root in inorder
        # Right subtree: elements after root in inorder
        
        # Build left and right subtrees recursively
        root.left = self.buildTree(preorder[1:1+root_idx], inorder[:root_idx])
        root.right = self.buildTree(preorder[1+root_idx:], inorder[root_idx+1:])
        
        return root
