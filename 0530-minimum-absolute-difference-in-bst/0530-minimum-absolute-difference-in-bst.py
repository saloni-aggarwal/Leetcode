# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
        
    def helper(self, root):
        # print("root =", root)
        if not root:
            return 
        
        self.helper(root.left)
        self.ans.append(root.val)
        self.helper(root.right)
        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        res = 1e9
        for i in range(1, len(self.ans)):
            res = min(res, self.ans[i] - self.ans[i-1])
        return res