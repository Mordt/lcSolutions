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
        if root == []:
            return []
        
        toReturn = []
        while root != Null:
            toReturn.append(root.val)
            if root.left <= root.right:
                root = root.left
            else:
                root = root.right
        

