# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMax(self, arr):
        maxIdx = 0
        for i in range(len(arr)):
            if arr[i] > arr[maxIdx]:
                maxIdx = i
        return maxIdx
    
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        maxIdx = self.findMax(nums)
        root = TreeNode(nums[maxIdx])
        root.left = self.constructMaximumBinaryTree(nums[:maxIdx])
        root.right = self.constructMaximumBinaryTree(nums[maxIdx+1:])
        return root
        
        