# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumChild(self, child, parent, grandparent, total):
        if child == None:
            return total
        if grandparent != None and grandparent.val % 2 == 0:
            total += child.val
        total = self.sumChild(child.left, child, parent, total)
        total = self.sumChild(child.right, child, parent, total)
        return total
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:     
        total = self.sumChild(root, None, None, 0)
        return total
             
