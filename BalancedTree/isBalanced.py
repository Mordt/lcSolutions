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
        #or recursively count height in subtrees
        #add function to calculate heights
        # is balanced if height.left is < height.right
        
        if root is None: return False #first edge case

        leftHeight = self.treeheight(root.left)
        rightHeight = self.treeHeight(root.right)
        
        if treeHeight -
        
        def treeHeight(self, root):
            if root is None: return 0
            return 1 + max(self.treeHeight(root.left), self.treeHeight(root.right))


