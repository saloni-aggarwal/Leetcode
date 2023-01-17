# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], left = -2**32, right = 2**32) -> bool:
        # print("root =", root)
        
        if not root:
            # print("in here")
            return True
        
        # print(type(right))
        
        if left < root.val and right > root.val:
            # print("in if")
            return self.isValidBST(root.left, left, root.val) and self.isValidBST(root.right, root.val, right)
        
        
        