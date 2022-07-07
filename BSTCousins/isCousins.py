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
        #two nodes are the same if they have different parents but equal depth
        #keep track of xdepth, ydepth
        #find xparent, yparent

        curr = root
        xdepth, ydepth = 0
        queue = deque()
        queue.append(curr)

        parMap = {}#map of nodes->parents
        parMap[curr] = None
        parMap[curr.left] = curr
        parMap[curr.right] = curr
        
        level = 0
        while True:

            curr = queue.pop(0)
            if curr == x:
                xdepth = level
            elif curr == y:
                ydepth == level

            else: #not x or y, populate map
                curr


            if curr.left: # if node->left is not null

                #do stuff
            if curr.right: # if node->right is not null
                #do stuff

        if xdepth == ydepth and parMap.get(x) != parMap.get(y): #if depth the same but diff parents
            return True
        else:
            return False

