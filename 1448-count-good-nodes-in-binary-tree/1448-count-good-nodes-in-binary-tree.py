# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
        
    def goodNodes(self, root: TreeNode, maxVal = float('-inf')) -> int:
        if root.val >= maxVal:
            maxVal = root.val
            self.ans += 1
        if root.left:
            self.goodNodes(root.left, maxVal)
        if root.right:
            self.goodNodes(root.right, maxVal)
        return self.ans