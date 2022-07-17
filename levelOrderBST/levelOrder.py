# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #level order needs a queue, a curr
        if root is None:
            return None
        
        curr = root
        queue = []
        queue.append(curr)
        
        while True:
            curr = queue.pop(0)
            print(curr)
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)


