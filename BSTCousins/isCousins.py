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

#leetcode so far:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root is None:
            return False

        #keep track of level
        xdepth = 0
        ydepth = 0

        queue = deque()
        curr = root
        queue.append(curr)
        level = 0

        #map to track nodes->parents
        nodeMap = {}
        nodeMap[curr.val] = None
        if curr.left:
            nodeMap[curr.left.val] = curr.val
        if curr.right:
            nodeMap[curr.right.val] = curr.val

        while len(queue) > 0:

            levelSize = len(queue)

            while(levelSize != 0):

                curr = queue.pop()
                #print(curr.val, level)

                if curr.val == x:
                    xdepth = level
                elif curr.val == y:
                    ydepth = level
                if xdepth != 0 and ydepth != 0:
                    break

                if curr.left:
                    queue.append(curr.left)
                    nodeMap[curr.left.val] = curr.val
                if curr.right:
                    queue.append(curr.right)
                    nodeMap[curr.right.val] = curr.val

                levelSize -= 1

            level += 1

        #checking if map works
        for key, value in nodeMap.items():
            print(key, value)

        print("x and y are ", x, y)

        # if depth the same but diff parents
        if xdepth == ydepth and nodeMap.get(x) != nodeMap.get(y):
            return True
        else:
            return False
