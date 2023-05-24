# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):
    
    def makeTree(self, root, val):
        if not root:
            return 
        self.seen.add(val)
        root.val = val
        self.makeTree(root.left, 2 * val + 1)
        self.makeTree(root.right, 2 * val + 2)
        # return root

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.seen = set()
        self.makeTree(root, 0)
        print(self.seen)
        
    def helper(self, root, target):
        if not root:
            return False
        if root.val == target:
            return True
        left = self.helper(root.left, target)
        right = self.helper(root.right, target)
        return left or right
            

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.seen
        
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)