# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        parents= set()
        children = set()
        
        nodes = {}
        
        for parent, child, left in descriptions:
            parents.add(parent)
            children.add(child)
            
            if parent in nodes:
                node = nodes[parent]
            else:
                node = TreeNode(parent)
                
            if child in nodes:
                childNode = nodes[child]
            else:
                childNode = TreeNode(child)
                
            if left:
                node.left = childNode
            else:
                node.right = childNode
                
            nodes[parent] = node
            nodes[child] = childNode
            
        return nodes[list(parents - children)[0]]