# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root):
        if not root:
            return 0, None
        depth1, left = self.helper(root.left)
        depth2, right = self.helper(root.right)
        
        if depth1 > depth2:
            return depth1+1, left
        elif depth1 < depth2:
            return depth2+1, right
        return depth1+1, root
        
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        _, ansRoot = self.helper(root)
        
        return ansRoot