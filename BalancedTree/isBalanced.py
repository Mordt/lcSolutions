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
        #tree is balanced if left and right subtrees differ in height by no more than 1
        #can do this by iterating through nodes, making a map of node->height
        #at end check if difference in height is > 1
        
