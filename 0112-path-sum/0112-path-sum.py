# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def hasPath(self, root, targetSum, currSum):
        if not root:            
            return False
        
        if currSum == targetSum and not root.left and not root.right:
            return True
        ans = False
        
        if root.left:
            ans = self.hasPath(root.left, targetSum, currSum + root.left.val) 
            
        if ans:
            return True
        
        if root.right:
            ans = self.hasPath(root.right, targetSum, currSum + root.right.val)
        
        if ans:
            return True
        
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.hasPath(root, targetSum, root.val)
        
            
        