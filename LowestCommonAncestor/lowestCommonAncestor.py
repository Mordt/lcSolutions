# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #defined as lowest node T that has both P and Q as descendants
        #nodes can be descendants of themselves
        #another key idea: find p and q initially by using sorted property of BST
        #if both in right/left subtree, change to there
        #if one in right and the other in left, lowest common ancestor is probably root

        if root is None:
            return None

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        else:  # neither unequivocally in left or right subtree, must be in diff subtrees
            return root
