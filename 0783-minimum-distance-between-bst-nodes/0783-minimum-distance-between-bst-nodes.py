# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        traversal = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            traversal.append(root.val)
            inorder(root.right)

        inorder(root)
        ans = float('inf')
        for i in range(len(traversal)-1,0,-1):
            ans = min(ans, traversal[i] - traversal[i-1])
        return ans
        
        