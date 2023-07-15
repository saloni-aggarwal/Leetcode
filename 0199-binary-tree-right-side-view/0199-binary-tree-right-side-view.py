# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        vals = []   
        seen = []
        if not root:
            return []
        seen.append(root)
        added = False
        
        while seen:
            temp = []            
            while seen:
                ele = seen.pop(0)
                if not added:
                    vals.append(ele.val)
                    added = True
                if ele.right:
                    temp.append(ele.right)
                if ele.left:
                    temp.append(ele.left)
                
            seen = temp
            added = False
            
        return vals
                
        
        