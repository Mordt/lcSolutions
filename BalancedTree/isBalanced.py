# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def treeHeight(self, root):
        if root is None: return 0
        return 1 + max(self.treeHeight(root.left), self.treeHeight(root.right))
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None: return False #first edge case

        lh = self.treeHeight(root.left)
        rh = self.treeHeight(root.right)
        
        if abs(lh - rh) <= 1 and self.isBalanced(root.left) is True and self.isBalanced(root.right) is True:
            return True
        
        return False


