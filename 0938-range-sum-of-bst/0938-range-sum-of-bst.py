# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # total = 0
    
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        
        def calSum(root, low, high):
            nonlocal total
            if root:
                if root.val >= low and root.val <= high:
                    total += root.val
                if root.val > low:
                    calSum(root.left, low, high)
                if root.val < high:
                    calSum(root.right, low, high)
        
        calSum(root, low, high)
        
        return total
            
        