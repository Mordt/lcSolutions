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
        
        #to keep track of x,y level
        xdepth = 0
        ydepth = 0
        
        queue = []
        curr = root
        queue.append(curr)
        level = 0
        
        #map to track nodes->parents
        nodeMap = {}
        nodeMap[curr.val] = (None, level)
        if curr.left:
            level += 1
            nodeMap[curr.left.val] = (curr.val, level)
            level -= 1
        if curr.right:
            level += 1
            nodeMap[curr.right.val] = (curr.val, level)
            level -= 1
        
        #checking if map works
        for key, value in nodeMap.items():
            print(key, value[0], value[1])
        
        while len(queue) > 0:
            found = False
            
            levelSize = len(queue)
            while(levelSize != 0):
                
                curr = queue.pop(0)
                
                if curr.val == x:
                    xdepth = level
                elif curr.val == y:
                    ydepth = level
                if xdepth != 0 and ydepth != 0:
                    found = True
                    break

                if curr.left:
                    queue.append(curr.left)
                    nodeMap[curr.left.val] = curr.val
                if curr.right:
                    queue.append(curr.right)
                    nodeMap[curr.right.val] = curr.val
                
                levelSize -= 1
            
            if found:
                break
            level += 1
            
        #print("xdepth and ydepth are ", xdepth, ydepth)
        
        if xdepth == ydepth and nodeMap.get(x) != nodeMap.get(y): #if depth the same but diff parents
            return True
        else:
            return False
