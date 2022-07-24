# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        #iterate recursively
        #use helper function to compare if subtrees are the same
        
    def isSameTree(self, s, t): #compares if s and t are the same 
        if not s and not t:
            return True
        
        if s and t and s.val == t.val:
            return (self.isSameTree(s.left, t.left) and 
                    self.isSameTree(s.right, t.right))
        
        return False

