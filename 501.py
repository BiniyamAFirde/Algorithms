# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.prev = None
        self.current_count = 0
        self.max_count = 0
        self.modes = []
        
        def in_order(node):
            if not node:
                return
            
            in_order(node.left)
            
            # Process current node
            if self.prev is not None and node.val == self.prev:
                self.current_count += 1
            else:
                self.current_count = 1
            
            # Update modes
            if self.current_count > self.max_count:
                self.max_count = self.current_count
                self.modes = [node.val]
            elif self.current_count == self.max_count:
                self.modes.append(node.val)
            
            self.prev = node.val
            
            in_order(node.right)
        
        in_order(root)
        return self.modes
