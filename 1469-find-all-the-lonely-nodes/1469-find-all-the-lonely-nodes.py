# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        
        def helper(root):
            if not root:
                return None
            left = helper(root.left)
            right = helper(root.right)

            # print("left =", left)
            # print("right =", right)
            if left and not right:
                # print("in if")               
                ans.append(left.val)
            elif right and not left:
                # print("in elif")
                ans.append(right.val)
            
            return root
        
        helper(root)
        return ans
        