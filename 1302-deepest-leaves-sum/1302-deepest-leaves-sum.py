# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def maxHeight(root, maxH, currH):
            if not root:
                maxH = max(maxH, currH)
                return maxH
            lHeight = maxHeight(root.left, maxH, currH+1)
            rHeight = maxHeight(root.right, maxH, currH+1)
            return max(lHeight, rHeight)
        
        def sumLeaves(root, currH, maxH, total):
            if not root:
                return 0
            if root and currH == maxH-1:
                return root.val
            total = sumLeaves(root.left, currH+1, maxH, total)
            total += sumLeaves(root.right, currH+1, maxH, total)
            return total
        
        maxH = maxHeight(root, 0, 0)
        return sumLeaves(root, 0, maxH, 0)
            
        