# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        
        def helper(root, lonely):
            
            if not root:
                return
            
            if lonely:
                ans.append(root.val)
            
            helper(root.left, root.right == None)
            helper(root.right, root.left == None)

            # if left and not right:             
            #     ans.append(left.val)
            # elif right and not left:
            #     ans.append(right.val)
            
            # return root
        
        helper(root, False)
        return ans
        