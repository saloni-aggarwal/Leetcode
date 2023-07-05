# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = collections.defaultdict(list)
    def helper(self, root):
        if not root:
            return -1
        left  = self.helper(root.left)
        right = self.helper(root.right)
        
        currHeight = 1 + max(left, right)
        Solution.ans[currHeight].append(root.val)
        return currHeight
    
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        Solution.ans = collections.defaultdict(list)
        self.helper(root)
        res = []
        for h in Solution.ans:
            res.append(Solution.ans[h])
        return res
        