# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """

        #level order traversal but keep track of node depth and
        #keep track of parent value
        #store node/level/parent
        
        queue = deque()
        nodeMap = defaultdict()
        queue.append((root, 0, 0))

        while True:

            if x in nodeMap and y in nodeMap:
                #do stuff

            if node.left: # if node->left is not null

                #do stuff
            if node.right: # if node->right is not null
                #do stuff


