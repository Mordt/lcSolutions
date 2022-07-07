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
                    level += 1
                    nodeMap[curr.left.val] = (curr.val, level)
                    level -= 1
                if curr.right:
                    queue.append(curr.right)
                    level += 1
                    nodeMap[curr.right.val] = (curr.val, level)
                    level -= 1
                
                levelSize -= 1
            
            if found:
                break
            level += 1
            
        #print("x is: ", x, nodeMap.get(x)[0])
        #checking if map works
        nodeParent = nodeMap.get(x)[0]
        nodeDepth = nodeMap.get(x)[1]
        
        for key in nodeMap:
            keyParent = nodeMap.get(key)[0]
            keyDepth = nodeMap.get(key)[1]
            
            if keyParent != nodeParent and keyDepth == nodeDepth:
                print(key)
        
        if xdepth == ydepth and nodeMap.get(x) != nodeMap.get(y): #if depth the same but diff parents
            return True
        else:
            return False
                       

