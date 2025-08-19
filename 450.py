# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Find inorder predecessor (largest in left subtree)
                predecessor = self.findMax(root.left)
                root.val = predecessor.val
                root.left = self.deleteNode(root.left, predecessor.val)
        
        return root
    
    def findMax(self, node):
        current = node
        while current.right:
            current = current.right
        return current
        
