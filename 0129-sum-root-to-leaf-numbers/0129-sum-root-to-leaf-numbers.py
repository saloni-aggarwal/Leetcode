# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def helper(st, root):
            if not root:
                return
            st = st * 10 + root.val
            
            if not root.left and not root.right:
                self.ans += st
                return 
            
            if root.left:
                helper(st, root.left)
                
            if root.right:
                helper(st, root.right)
                
        helper(0, root)
        return self.ans