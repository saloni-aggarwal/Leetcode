# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findDepth(self, maxDepth, currDepth, root):
        if root == None:
            if currDepth > maxDepth:
                maxDepth = currDepth
            return maxDepth
        maxDepth = self.findDepth(maxDepth, currDepth + 1, root.left)
        maxDepth = self.findDepth(maxDepth, currDepth + 1, root.right) 
        return maxDepth

    def findSum(self, maxDepth, maxSum, currDepth, root):
        if root == None:
            return maxSum
        if currDepth == maxDepth:       
            maxSum += root.val
        maxSum = self.findSum(maxDepth, maxSum, currDepth + 1, root.left)
        maxSum = self.findSum(maxDepth, maxSum, currDepth + 1, root.right) 
        return maxSum 
         

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        maxDepth = self.findDepth(0, 0, root)
        maxSum = self.findSum(maxDepth, 0, 1, root)
        return maxSum