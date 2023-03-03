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
        
        elif currSum == targetSum and not root.left and not root.right:
            return True
        
        if root.left:
            if self.hasPath(root.left, targetSum, currSum + root.left.val):
                return True
        
        if root.right:
            if self.hasPath(root.right, targetSum, currSum + root.right.val):
                return True
        
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.hasPath(root, targetSum, root.val)
        
            
        