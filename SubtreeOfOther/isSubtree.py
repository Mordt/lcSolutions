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
        
        if not subroot: return True 
        if not root: return False
        
        if self.isSametree(root, subroot):
            return True
        else:
            return (self.isSubtree(root.left, subroot) or
                    self.isSubtree(root.right, subroot))
        
    def isSametree(self, s, t): #compares if s and t are the same 
        if not s and not t:
            return True
        
        if s and t and s.val == t.val:
            return (self.isSametree(s.left, t.left) and 
                    self.isSametree(s.right, t.right))
        
        return False
    
