# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return None
        
        stack = []
        curr = root
        
        while True:
            #if curr is not null, add to stack
            #keep going till end is reached
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            
            
            
