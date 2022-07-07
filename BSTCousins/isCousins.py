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

        queue = []
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

                curr = queue.pop(0)

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
        #for key, value in nodeMap.items():
        #    print(key, value)
        #print("xdepth and ydepth are ", xdepth, ydepth)

        # if depth the same but diff parents
        if xdepth == ydepth and nodeMap.get(x) != nodeMap.get(y):
            return True
        else:
            return False
