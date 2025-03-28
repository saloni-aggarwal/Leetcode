"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        if len(tree) == 1:
            return tree[0]
        
        children = set()
        
        for node in tree:
            if node.children:
                children.update(node.children)
        
        for p in tree:
            if p not in children:
                return p
            
        return None
        