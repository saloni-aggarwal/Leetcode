# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def helper(self, root1, root2):
        # if not root1 and not root2:
        #     return None
        # val = 0
        # if root1:
        #     val += root1.val
        # if root2:
        #     val += root2.val
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.helper(root1.left, root2.left)
        root1.right = self.helper(root1.right, root2.right)
            
        # root = TreeNode(val)
        
        # if root1 and root2:
        #     root.left = self.helper(root1.left, root2.left)
        #     root.right = self.helper(root1.right, root2.right)
        # elif root1:
        #     root.left = self.helper(root1.left, None)
        #     root.right = self.helper(root1.right, None)
        # elif root2:
        #     root.left = self.helper(None, root2.left)
        #     root.right = self.helper(None, root2.right)
            
        return root1
        
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.helper(root1, root2)