# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None: return False #first edge case

        leftHeight = self.treeheight(root.left)
        rightHeight = self.treeHeight(root.right)
        
        if abs((leftHeight-rightHeight) <= 1) and 
            isBalanced(root.left) is True and
            isBalanced(root.right) is True:
                return True
        
        return False

        def treeHeight(self, root):
            if root is None: return 0
            return 1 + max(self.treeHeight(root.left), self.treeHeight(root.right))
        
        
