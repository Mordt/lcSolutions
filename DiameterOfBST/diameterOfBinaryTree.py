# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #possible level order traversal
        #depth of left + depth of right
        #left right root, so postorder?
        #use max value that's updated as u go
        
        if root == None:
            return 0
        
        queue = []
        curr = root
        queue.append(curr)
        
        while True:
            curr = queue.pop(0)
        
