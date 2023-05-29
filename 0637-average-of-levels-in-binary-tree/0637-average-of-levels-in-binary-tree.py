# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        bfs = []
        
        bfs.append(root)
        ans = []
        
        while bfs:
            tempBfs = []
            total = 0
            for n in bfs:
                total += n.val
                if n.left:
                    tempBfs.append(n.left)
                if n.right:
                    tempBfs.append(n.right)
            
            ans.append(total/len(bfs))
            
            bfs = tempBfs
            
        return ans
                