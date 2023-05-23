"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution(object):
    def cloneTree(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        
        copy = Node(root.val)
        
        for child in root.children:
            copy.children.append(self.cloneTree(child))
        
        # print(copy.val, "  ", copy.children)
            
        return copy
            
        