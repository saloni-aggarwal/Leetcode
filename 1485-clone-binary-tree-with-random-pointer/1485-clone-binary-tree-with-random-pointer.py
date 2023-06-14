# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    
    def __init__(self):
        self.seen: dict[str, int] = {None: None}
    
    def helper(self, root):
        if not root:
            return None
        
        if self.seen.get(root) is not None:
            return self.seen.get(root)
        
        newRoot = NodeCopy(root.val)
        
        self.seen[root] = newRoot
        newRoot.left = self.helper(root.left)
        newRoot.right = self.helper(root.right)
        newRoot.random = self.helper(root.random)
        
        return newRoot
        
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        
        newRoot = self.helper(root)
        return newRoot
        