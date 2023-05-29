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
            count = length = len(bfs)
            total = 0
            while count > 0:
                n = bfs.pop(0)
                total += n.val
                if n.left:
                    bfs.append(n.left)
                if n.right:
                    bfs.append(n.right)
                count -= 1
            
            ans.append(total/length)
            
            # bfs = tempBfs
            
        return ans
                